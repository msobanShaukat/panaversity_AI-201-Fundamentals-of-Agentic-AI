from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import os

model = SentenceTransformer('all-MiniLM-L6-v2')


def _quality_weight(q):
    return {"High": 3, "Medium": 2, "Low": 1}.get(q, 1)


def _get_openai_client():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return None
    return OpenAI(api_key=key)


def semantic_conflict_detection(findings, threshold=0.35):
    """
    findings: list[section], each having 'findings': list[{'text': ...}]
    """
    all_texts = [(i, f['text']) for i, result in enumerate(findings) for f in result['findings']]
    texts = [t for _, t in all_texts]
    if len(texts) < 2:
        return [], []
    embeddings = model.encode(texts)
    conflicts, explanations = [], []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            # Cast to float to avoid numpy formatting errors
            sim = float(cosine_similarity([embeddings[i]], [embeddings[j]])[0, 0])
            if sim > 0.85:
                continue
            if sim < threshold and len(texts[i]) > 30 and len(texts[j]) > 30:
                conflicts.append((i, j, sim, texts[i], texts[j]))
                explanations.append(
                    f"Agent finding {i+1} and finding {j+1} present potentially contradictory statements: "
                    f"\n - \"{texts[i][:90]}...\" \n - \"{texts[j][:90]}...\"\n(semantic similarity: {sim:.2f})."
                )
    return conflicts, explanations


def generate_section_summary(section_title, findings, instructions=None, refs_map=None):
    instructions = instructions or {}
    persona = instructions.get("persona", {})
    style = persona.get("style", "concise")
    name = persona.get("name") or "the reader"
    city = persona.get("city") or ""
    topic = persona.get("topic") or ""
    temperature = instructions.get("temperature", 0.3)
    max_tokens = instructions.get("summary_max_tokens", 150)

    texts = [f["text"] for f in findings]
    if not texts:
        return "No information found for this perspective."

    used_urls = [f.get("url") for f in findings if f.get("url")]
    used_nums = [str(refs_map.get(u)) for u in used_urls if refs_map and refs_map.get(u)]
    sources_line = f" Sources: [{']['.join(used_nums)}]" if used_nums else ""

    prompt = (
        f"Summarize the findings for '{section_title}' in a {style} style for {name} from {city} who is interested in {topic}. "
        f"Prioritize high-quality sources, keep it crisp, and include trade-offs. End with 1 sentence takeaway.{sources_line}\n\n"
        f"Findings:\n" + "\n".join([f"- {tx}" for tx in texts])
    )

    client = _get_openai_client()
    if not client:
        lead = texts[:300]
        return f"Summary (no-LLM fallback): {lead}..."

    try:
        stream = client.chat.completions.create(
            model=instructions.get("model", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        out = []
        for chunk in stream:
            delta = getattr(chunk.choices, "delta", None)
            if delta and getattr(delta, "content", None):
                part = delta.content
                print(part, end="", flush=True)
                out.append(part)
        print()
        return "".join(out).strip() or "Summary unavailable."
    except Exception as e:
        lead = texts[:300]
        return f"(Summary generation failed: {str(e)}) {lead}..."


class SynthesisAgent:
    def synthesize(self, research_results, instructions=None, refs_map=None):
        instructions = instructions or {}
        refs_map = refs_map or {}
        synthesis_lines = []

        for idx, result in enumerate(research_results, 1):
            synthesis_lines.append(f"\n#### {result['question']}")
            findings_sorted = sorted(result['findings'], key=lambda f: _quality_weight(f["quality"]), reverse=True)

            summary_input = []
            for i, f in enumerate(findings_sorted, 1):
                url = f.get('url', '')
                q = f.get('quality', 'Low')
                citation = f"[Source]({url})"
                synthesis_lines.append(f"{i}. {f['text']} {citation} (Quality: {q})")
                summary_input.append(f)

            summary = generate_section_summary(
                result["question"],
                summary_input,
                instructions=instructions,
                refs_map=refs_map,
            )
            synthesis_lines.append(f"\n> **Section Summary:** {summary}\n")

        conflicts, explanations = semantic_conflict_detection(research_results)
        all_conflict_explanations = "\n".join(explanations)
        return '\n'.join(synthesis_lines), explanations, all_conflict_explanations
