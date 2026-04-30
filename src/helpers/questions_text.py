"""Prompt templates for AI-generated anatomy questions."""

UBA_DIVERSITY_MODES = [
    "clinical_case",
    "conceptual_reasoning",
    "functional_analysis",
    "lesion_analysis",
    "comparative"
]

ANATOMY_QUESTION = (
    "You are a senior medical professor specialized in Human Anatomy and an expert "
    "in designing high-difficulty multiple-choice exam questions for UBA medical exams.\n\n"

    "TASK:\n"
    "Generate EXACTLY ONE high-quality multiple-choice question.\n\n"

    "SOURCE CONSTRAINT:\n"
    "Base the question strictly on the following references:\n"
    "- Latarjet & Ruiz Liard\n"
    "- Netter Atlas\n"
    "- Rouvière & Delmas\n"
    "- Pró\n\n"

    "TOPIC:\n"
    "{TOPIC}\n\n"

    "DIVERSITY MODE:\n"
    "{DIVERSITY_MODE}\n\n"

    "ANTI-REPETITION:\n"
    "Avoid similarity with:\n"
    "{RECENT_QUESTIONS}\n\n"

    "QUALITY REQUIREMENTS:\n"
    "- The question must require reasoning, not recall\n"
    "- Use clinically relevant or functional context when possible\n"
    "- Avoid obvious or trivial patterns\n"
    "- Avoid generic textbook phrasing\n\n"

    "DISTRACTOR RULES (VERY IMPORTANT):\n"
    "- All incorrect options must be plausible\n"
    "- Each distractor must be close to the correct answer conceptually\n"
    "- Avoid obviously wrong answers\n"
    "- Avoid different categories (e.g., mixing nerves with bones incorrectly)\n\n"

    "CRITICAL VALIDATION (DO THIS INTERNALLY BEFORE ANSWERING):\n"
    "1. Ensure ONLY ONE option is correct\n"
    "2. Ensure no ambiguity exists\n"
    "3. Ensure all distractors are competitive\n"
    "4. If any issue is found, FIX the question before output\n\n"

    "LANGUAGE:\n"
    "- Rioplatense Spanish\n\n"

    "OUTPUT RULES (STRICT):\n"
    "- Return ONLY valid JSON\n"
    "- No extra text before or after\n"
    "- No comments\n"
    "- No trailing commas\n\n"

    "JSON STRUCTURE:\n"
    "{"
    "\"question\": \"...\","
    "\"answer_a\": \"...\","
    "\"answer_b\": \"...\","
    "\"answer_c\": \"...\","
    "\"answer_d\": \"...\","
    "\"explanation_a\": \"...\","
    "\"explanation_b\": \"...\","
    "\"explanation_c\": \"...\","
    "\"explanation_d\": \"...\","
    "\"correct_answer\": \"A|B|C|D\""
    "}\n\n"

    "FINAL CHECK (MANDATORY):\n"
    "- Output must be valid JSON\n"
    "- Exactly 4 options\n"
    "- Exactly 1 correct answer\n"
)
