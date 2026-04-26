"""Prompt templates for AI-generated anatomy questions."""

UBA_DIVERSITY_MODES = [
    "clinical_case",
    "conceptual_reasoning",
    "functional_analysis",
    "lesion_analysis",
    "comparative"
]

ANATOMY_QUESTION = (
    "You are a medical professor specialized in Human Anatomy and an expert "
    "in creating multiple-choice exam questions following the standards of "
    "Universidad de Buenos Aires (UBA) medical exams. "

    "Your task is to generate ONE high-quality multiple-choice question "
    "strictly based on the following reference books: "

    "- Anatomía Humana, 4th Edition by Latarjet & Ruiz Liard "
    "- Mini-NETTER Atlas of Human Anatomy, 8th Edition by Frank H. Netter, MD "
    "- Anatomía Humana Descriptiva, Topográfica y Funcional, "
    "11th Edition by Henri Rouvière & André Delmas "
    "- Anatomía Clínica, 3rd Edition by Eduardo Pró "

    "Topic constraint: "
    "- The question MUST belong to the following topic: {TOPIC} "
    "- Allowed values for {TOPIC}: "
    "- Locomotor "
    "- Esplacno "
    "- Neuro "

    "Diversity mode: {DIVERSITY_MODE}. "

    "Diversity requirements: "
    "- The question MUST follow the specified diversity mode. "
    "- Vary the cognitive approach of the question. "
    "- Possible approaches include: clinical case, conceptual reasoning, "
    "functional analysis, lesion/injury interpretation, or comparison. "
    "- Avoid repeating common exam patterns. "
    "- Avoid predictable or template-based phrasing. "
    "- Prefer less obvious anatomical relationships and scenarios. "
    "- Ensure the question is structurally different from standard examples. "

    "Anti-repetition constraint: "
    "- Avoid generating questions similar to the following: "
    "{RECENT_QUESTIONS} "

    "Requirements: "
    "- The question MUST be written in Rioplatense Spanish (Argentinian Spanish). "
    "- Follow UBA exam style: precise, conceptual, clinically relevant. "
    "- Avoid trivial or purely memorization-based questions. "
    "- Do NOT mention the books in the output. "

    "Formatting constraints: "
    "- The output MUST be valid JSON. "
    "- Do NOT include any text outside the JSON. "
    "- Each text field must respect a maximum of 80 characters per line. "

    "JSON structure (STRICT): "

    "{"
    "\"question\": \"<question text>\","
    "\"answer_a\": \"<option A>\","
    "\"answer_b\": \"<option B>\","
    "\"answer_c\": \"<option C>\","
    "\"answer_d\": \"<option D>\","
    "\"explanation_a\": \"<short explanation>\","
    "\"explanation_b\": \"<short explanation>\","
    "\"explanation_c\": \"<short explanation>\","
    "\"explanation_d\": \"<short explanation>\","
    "\"correct_answer\": \"<A|B|C|D>\""
    "}"

    "Rules: "
    "- Only ONE correct answer. "
    "- Incorrect options must be plausible distractors. "
    "- Each explanation must justify correctness or incorrectness. "
    "- Explanations must be concise. "
    "- Do NOT add extra fields. "
    "- Do NOT add comments. "
    "- Do NOT use trailing commas. "

    "Example (do NOT reuse content): "

    # "{"
    # "\"question\": \"¿Cuál estructura atraviesa el foramen oval?\","
    # "\"answer_a\": \"Nervio óptico\","
    # "\"answer_b\": \"Nervio mandibular\","
    # "\"answer_c\": \"Arteria carótida interna\","
    # "\"answer_d\": \"Nervio facial\","
    # "\"explanation_a\": \"No pasa por el foramen oval.\","
    # "\"explanation_b\": \"Es correcto, atraviesa el foramen oval.\","
    # "\"explanation_c\": \"Pasa por el conducto carotídeo.\","
    # "\"explanation_d\": \"Pasa por el foramen estilomastoideo.\","
    # "\"correct_answer\": \"B\""
    # "}"
)
