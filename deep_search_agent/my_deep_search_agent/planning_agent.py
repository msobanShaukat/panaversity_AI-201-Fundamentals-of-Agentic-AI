class PlanningAgent:
    def plan(self, question, user_profile=None):
        core = (question or "").strip("?")

        if "pros and cons" in core.lower():
            return [
                f"{core}? (Benefits for organizations)",
                f"{core}? (Potential risks or downsides)",
                f"{core}? (How does it affect workers?)",
            ]

        if "climate change" in core.lower():
            return [
                f"{core} - Environmental Impacts",
                f"{core} - Effects on Agriculture",
                f"{core} - Policy and Economic Trends",
            ]

        if user_profile and user_profile.get("interest"):
            return [
                f"{core} - impact on {user_profile['interest']}",
                f"{core} - global trends",
                f"{core} - local perspective",
            ]

        return [
            f"{core} [Perspective 1]",
            f"{core} [Perspective 2]",
            f"{core} [Perspective 3]",
        ]
