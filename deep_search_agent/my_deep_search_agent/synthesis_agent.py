import os
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the sentence transformer model for semantic analysis
model = SentenceTransformer('all-MiniLM-L6-v2')

def _quality_weight(q: str) -> int:
    """Assigns a numeric weight to a source's quality rating."""
    return {"High": 5, "Medium": 3, "Low": 1}.get(q or "Low", 1)

def _get_gemini_client():
    """
    Initializes and returns a Gemini client if the GOOGLE_API_KEY is available.
    """
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        return None
    try:
        genai.configure(api_key=key)
        # Using a common, capable model. Adjust if needed.
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        print(f"[ERROR] Failed to configure Gemini client: {e}")
        return None

def semantic_conflict_detection(findings, threshold=0.35):
    """
    Detects potential semantic conflicts between different text findings.
    """
    all_texts = [(i, f['text']) for i, result in enumerate(findings) for f in result['findings']]
    texts = [t for _, t in all_texts]
    if len(texts) < 2:
        return [], []

    embeddings = model.encode(texts)
    conflicts, explanations = [], []

    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
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

def _filter_low_quality_for_summary(findings):
    """
    Prefers excluding Low quality items from the summary if enough higher-quality sources exist.
    """
    non_low = [f for f in findings if (f.get("quality") or "Low") != "Low"]
    return non_low if len(non_low) >= 2 else findings

def generate_section_summary(section_title, findings, instructions=None, refs_map=None):
    """
    Generates a summary for a section using the Gemini API, with a corrected offline fallback.
    """
    instructions = instructions or {}
    persona = instructions.get("persona", {})
    style = persona.get("style", "concise")
    name = persona.get("name") or "the reader"
    city = persona.get("city") or ""
    topic = persona.get("topic") or ""
    temperature = instructions.get("temperature", 0.3)
    max_tokens = instructions.get("summary_max_tokens", 150)

    findings_for_summary = _filter_low_quality_for_summary(findings)
    texts = [f["text"] for f in findings_for_summary]

    if not texts:
        return "No information found for this perspective."

    used_urls = [f.get("url") for f in findings_for_summary if f.get("url")]
    used_nums = [str(refs_map.get(u)) for u in used_urls if refs_map and refs_map.get(u)]
    sources_line = f" Sources: [{']['.join(used_nums)}]" if used_nums else ""

    prompt = (
        f"Summarize the findings for '{section_title}' in a {style} style for {name} from {city} who is interested in {topic}. "
        f"Prioritize high-quality sources, keep it crisp, and include trade-offs. End with 1 sentence takeaway.{sources_line}\n\n"
        f"Findings:\n" + "\n".join([f"- {tx}" for tx in texts])
    )

    client = _get_gemini_client()

    # **CORRECTED FALLBACK LOGIC**
    if not client:
        print("[INFO] Gemini client not available. Using offline summarizer fallback.")
        # Correctly slices the first string, not the list
        lead = texts[0][:300] if isinstance(texts[0], str) else ""
        return f"Summary (no-LLM fallback): {lead}..."

    try:
        # **GEMINI API CALL**
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature
        )
        # Using stream=True for real-time feel
        stream = client.generate_content(prompt, stream=True, generation_config=generation_config)

        out = []
        for chunk in stream:
            if chunk.text:
                part = chunk.text
                print(part, end="", flush=True) # Prints tokens as they arrive
                out.append(part)
        print() # Newline after streaming is complete
        return "".join(out).strip() or "Summary unavailable."
    
    except Exception as e:
        print(f"[ERROR] Summary generation with Gemini failed: {str(e)}")
        # Fallback on error, also with the corrected string slicing
        lead = texts[0][:300]
        return f"(Summary generation failed: {str(e)}) {lead}..."

class SynthesisAgent:
    def synthesize(self, research_results, instructions=None, refs_map=None):
        """
        Synthesizes research results into a structured report with summaries and conflict detection.
        """
        instructions = instructions or {}
        refs_map = refs_map or {}
        synthesis_lines = []

        for idx, result in enumerate(research_results, 1):
            synthesis_lines.append(f"\n#### {result['question']}")
            
            findings_sorted = sorted(result['findings'], key=lambda f: _quality_weight(f.get("quality")), reverse=True)
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
