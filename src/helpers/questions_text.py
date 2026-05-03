"""
    Prompt templates for AI-generated anatomy questions.

    Bibliography used on prompt and topics generation:

    - Anatomía Humana, 4th Edition by Latarjet & Ruiz Liard
    
    - Mini-NETTER Atlas of Human Anatomy, 8th Edition by Frank H. Netter, MD
    
    - Anatomía Humana Descriptiva, Topográfica y Funcional 11th Edition by 
        Henri Rouvière & André Delmas
    
    - Anatomía Clínica, 3rd Edition by Eduardo Pró
"""

UBA_DIVERSITY_MODES = [
    "identification",
    "relationship",
    "location",
    "function",
    "innervation",
    "vascularization",
    "exception"
]

LOCOMOTOR_DESCRIPTIONS = {
    "osteologia_general": "estructura, tipos de huesos, osificación, irrigación e inervación ósea",
    "osteologia_miembro_superior": "huesos del miembro superior, accidentes óseos, relaciones, relieves y funciones", # pylint: disable=line-too-long
    "osteologia_miembro_inferior": "huesos del miembro inferior, accidentes óseos, relaciones, relieves y funciones", # pylint: disable=line-too-long
    "osteologia_columna_vertebral": "vértebras, características regionales y articulación",
    "osteologia_torax": "esternón, costillas y su organización estructural",
    "osteologia_craneo": "huesos del cráneo, base y bóveda, forámenes",

    "articulaciones_general": "tipos articulares, movimientos y estructuras asociadas",
    "articulaciones_miembro_superior": "articulaciones del miembro superior y sus movimientos",
    "articulaciones_miembro_inferior": "articulaciones del miembro inferior y sus movimientos",
    "articulaciones_columna": "articulaciones vertebrales y discos intervertebrales",
    "articulaciones_craneo": "suturas y articulaciones craneales",

    "miologia_general": "tipos musculares, inserciones, irrigación e inervación",
    "musculos_miembro_superior": "músculos del miembro superior y sus funciones",
    "musculos_miembro_inferior": "músculos del miembro inferior y sus funciones",
    "musculos_espalda": "músculos superficiales y profundos del dorso y nuca",

    "compartimentos_brazo": "compartimentos anterior y posterior del brazo",
    "compartimentos_antebrazo": "compartimentos flexor y extensor",
    "compartimentos_mano": "compartimentos musculares de la mano",
    "compartimentos_muslo": "compartimentos del muslo",
    "compartimentos_pierna": "compartimentos de la pierna",
    "compartimentos_pie": "compartimentos del pie",

    "arterias_miembro_superior": "irrigación arterial del miembro superior",
    "arterias_miembro_inferior": "irrigación arterial del miembro inferior",
    "venas_miembro_superior": "drenaje venoso superficial y profundo superior",
    "venas_miembro_inferior": "drenaje venoso superficial y profundo miembro inferior",

    "plexo_braquial": "formación, ramos colaterales y profundos y territorios del plexo braquial",
    "nervios_miembro_superior": "inervación completa del miembro superior y recurridos de los nervios principales", # pylint: disable=line-too-long
    "nervios_miembro_inferior": "inervación completa del miembro inferior y recurridos de los nervios principales", # pylint: disable=line-too-long

    "axila": "límites, contenido y relaciones de la axila",
    "region_deltoidea": "limites y contenidos de la región deltoidea",
    "fosa_cubital": "límites y contenidos de la fosa cubital",
    "canal_carpiano": "contenidos y límites del túnel carpiano",
    "triangulo_femoral": "límites y contenido del triángulo femoral",
    "conducto_aductor": "trayecto, limites y contenido del conducto aductor",
    "fosa_poplitea": "límites y contenidos de la fosa poplítea",

    "regiones_topograficas_miembro_superior": "regiones del miembro superior",
    "regiones_topograficas_miembro_inferior": "regiones del miembro inferior",

    "linfaticos_miembro_superior": "drenaje linfático del miembro superior",
    "linfaticos_miembro_inferior": "drenaje linfático del miembro inferior",
    "linfaticos_dorso": "linfáticos del dorso",
    "linfaticos_nuca": "drenaje linfático de la región nucal",

    "planimetria": "division del cuerpo en ejes y planes"
}

SPLACHNOLOGY_DESCRIPTIONS = {

    "regiones_topograficas_cabeza": "división anatómica superficial de la cabeza",
    "regiones_topograficas_cuello": "triángulos cervicales y contenidos",
    "regiones_topograficas_tronco": "regiones del tronco y referencias anatómicas",

    "cavidad_oral": "estructura, límites y contenido de la cavidad oral",
    "lengua": "músculos, inervación y vascularización de la lengua",
    "glandulas_salivales": "glándulas mayores y menores, drenaje y función",
    "faringe": "divisiones, músculos, inervación e irrigación",
    "esofago": "trayecto, inervación, irrigación y relaciones",
    "estomago": "regiones, relaciones, irrigación e inervación",
    "intestino_delgado": "duodeno, yeyuno e íleon",
    "intestino_grueso": "colon, ciego y recto",
    "higado": "segmentación, irrigación y drenaje",
    "vias_biliares": "conductos biliares y drenaje",
    "vesicula_biliar": "estructura e irrigación",
    "pancreas": "regiones, función e irrigación",

    "cavidad_nasal": "estructura y límites",
    "senos_paranasales": "estructura y límites",
    "laringe": "cartílagos, músculos, irrigación e inervación",
    "traquea": "estructura y relaciones",
    "bronquios": "estructura y relaciones",
    "pulmones": "lóbulos, segmentación, relaciones, irrigación e inervación",
    "pleura": "hojas pleurales y cavidad",

    "rinon": "estructura, relaciones e irrigación",
    "ureter": "trayecto, relacionesl ley de lushka y estrechamientos",
    "vejiga": "estructura, irrigación, inervación y relaciones",
    "uretra": "porciones, musculos, inervación, irrigación y diferencias sexuales",

    "testiculo": "relaciones, irrigación e inervación",
    "epididimo": "trayecto y relaciones",
    "conducto_deferente": "trayecto y relaciones",
    "vesiculas_seminais": "relaciones y trayecto",
    "prostata": "estructura, irrigación e inervación",
    "pene": "periné, estructura, vascularización e inervación",

    "ovario": "relaciones, ligamentos, irrigación e inervación",
    "trompas_uterinas": "segmentos, relaciones, ligamentos, irrigación e inervación",
    "utero": "segmentos, relaciones, ligamentos, irrigación e inervación",
    "vagina": "estructura, relaciones, ligamentos, irrigación e inervación",
    "genitales_externos_femeninos": "periné, vulva, componentes, irrigación e inervación",

    "peritoneo": "hojas y cavidad peritoneal",
    "mesenterios": "fijación de vísceras",
    "epiplones": "omento mayor y menor",
    "retroperitoneo": "órganos retroperitoneales",
    "peritoneo_fascia_coalescencia": "fascias de coalescencia y fijación",

    "linfatico_abdominal": "drenaje linfático abdominal",
    "linfatico_toracico": "linfáticos torácicos",
    "conducto_toracico": "trayecto y drenaje",
    "ganglios_linfaticos_abdominales": "grupos ganglionares abdominales",
    "ganglios_linfaticos_toracicos": "ganglios torácicos",

    "linfaticos_cabeza_cuello": "drenaje linfático de cabeza y cuello",
    "linfaticos_pelvicos": "linfáticos de pelvis",
    "linfaticos_abdominales_detallados": "red linfática abdominal detallada",
    "linfaticos_toracicos_detallados": "red linfática torácica",

    "drenaje_venoso_superficial_abdominal": "venas superficiales abdominales",
    "drenaje_venoso_profundo_abdominal": "sistema venoso profundo abdominal",
    "drenaje_venoso_superficial_pelvico": "venas superficiales pélvicas",
    "drenaje_venoso_profundo_pelvico": "drenaje venoso profundo pélvico",

    "irrigacion_digestivo": "arterias del sistema digestivo",
    "irrigacion_respiratorio": "vascularización respiratoria",
    "irrigacion_pelvico": "arterias pélvicas",

    "musculos_cabeza": "músculos faciales y masticadores",
    "musculos_cuello": "músculos cervicales y sus funciones",
    "musculos_torax": "músculos intercostales y respiratorios",
    "musculos_abdomen": "músculos de la pared abdominal",
    "musculatura_abdominal": "función y organización muscular abdominal",
    "musculatura_respiratoria": "músculos respiratorios",
    "musculatura_pelvica": "suelo pélvico",

    "plexo_lumbar": "formation de nervios, ramas y sus recurridos del plexo lumbar",
    "plexo_sacro": "formación de nervios, ramas y sus recurridos del plexo sacro",
}

NEURO_DESCRIPTIONS = {
    "medula_espinal": "LCR, segmentos, sustancia gris y blanca",
    "tronco_encefalico": "mesencéfalo, puente y bulbo",
    "bulbo_raquideo": "núcleos y funciones",
    "puente": "estructura y conexiones",
    "mesencefalo": "pedúnculos y colículos",

    "cerebelo": "lóbulos y funciones",
    "diencefalo": "tálamo e hipotálamo",
    "talamus": "núcleos y funciones",
    "hipotalamo": "control autonómico",

    "telencefalo": "hemisferios cerebrales",
    "corteza_cerebral": "áreas funcionales, giros y surcos",
    "lobulos_cerebrales": "división cortical",
    "ganglios_basales": "núcleos profundos",

    "vias_motoras": "vías descendentes",
    "vias_piramidales": "tracto corticoespinal",
    "vias_extrapiramidales": "control motor involuntario",
    "vias_sensitivas": "vías ascendentes",

    "nervios_craneales": "pares craneales, trayectos y funciones",
    "nervio_olfatorio": "via, trayectos y funciones",
    "nervio_optico": "via, trayectos y funciones",
    "nervio_oculomotor": "via, trayectos y funciones",
    "nervio_troclear": "via, trayectos y funciones",
    "nervio_trigemino": "via, trayectos y funciones",
    "nervio_abducens": "via, trayectos y funciones",
    "nervio_facial": "via, trayectos y funciones",
    "nervio_vestibulococlear": "via, trayectos y funciones",
    "nervio_glosofaringeo": "via, trayectos y funciones",
    "nervio_vago": "via, trayectos y funciones",
    "nervio_accesorio": "via, trayectos y funciones",
    "nervio_hipogloso": "via, trayectos y funciones",

    "sistema_nervioso_autonomo": "simpático y parasimpático",
    "simpatico": "respuestas de alerta",
    "parasimpatico": "funciones viscerales",

    "meninges": "duramadre, aracnoides y piamadre",
    "liquido_cefalorraquideo": "producción y circulación",
    "ventriculos_cerebrales": "sistema ventricular",

    "irrigacion_cerebral": "arterias cerebrales",
    "circulo_de_willis": "anastomosis arterial",
    "senos_venosos": "drenaje venoso",

    "ojo": "estructura ocular",
    "oido": "oído externo, medio e interno",
    "vias_opticas": "trayecto visual",
    "vias_auditivas": "trayecto auditivo",

    "drenaje_venoso_superficial_cerebral": "venas superficiales",
    "drenaje_venoso_profundo_cerebral": "sistema venoso profundo",

    "drenaje_linfatico_cerebral": "drenaje linfático encefálico",

    "sistema_vertebrobasilar": "arterias vertebrales y basilar",

    "irrigacion_cerebral_detallada": "ramas arteriales y sus porciones cerebrales detalladas"
}

ANATOMY_QUESTION = (
    "You are a senior medical professor specialized in Human Anatomy and an expert "
    "in designing multiple-choice questions that STRICTLY follow the style of UBA exams.\n\n"

    "TASK:\n"
    "- Generate EXACTLY ONE high-quality multiple-choice question.\n"
    "- You MUST ALWAYS generate a valid question (never return placeholders or error messages).\n\n"

    "TOPIC:\n"
    "{TOPIC}\n\n"

    "SUB TOPIC (STRICT FOCUS):\n"
    "{SUB_TOPIC}\n\n"

    "SUB TOPIC DESCRIPTION (AUTHORITATIVE SCOPE):\n"
    "{SUBTOPIC_DESCRIPTION}\n\n"

    "DIVERSITY MODE:\n"
    "{DIVERSITY_MODE}\n\n"

    "ANTI-REPETITION:\n"
    "{RECENT_QUESTIONS}\n\n"

    "CORE REQUIREMENTS:\n"
    "- The question MUST be short and direct\n"
    "- Test ONLY ONE concept\n"
    "- No clinical cases\n"
    "- No unnecessary context\n\n"

    "DOMAIN ENFORCEMENT (HARD CONSTRAINT):\n"
    "- The question MUST stay strictly within {SUB_TOPIC}\n"
    "- Use ONLY anatomical elements compatible with {SUBTOPIC_DESCRIPTION}\n"
    "- If the subtopic is narrow, ADAPT the question (do NOT expand scope)\n"
    "- If alignment is not possible, REFORMULATE the question (never change topic)\n"
    "- NEVER generate meta-text (e.g., 'missing topic', 'cannot generate')\n\n"

    "ANATOMICAL CONSISTENCY (STRICT):\n"
    "- All answer options MUST belong to the SAME anatomical category\n"
    "- All options must be mutually exclusive\n"
    "- NO duplicated answers\n"
    "- NO partially correct answers\n"
    "- NO ambiguous or controversial answers\n"
    "- Use precise and standard anatomical terminology\n\n"

    "UNIQUENESS VALIDATION (CRITICAL):\n"
    "- There MUST be ONLY ONE correct answer\n"
    "- All other options MUST be clearly incorrect\n"
    "- If more than one option could be correct, REWRITE the question\n"
    "- The question MUST NOT depend on interpretation or context\n\n"

    "ANSWER CONSISTENCY CHECK (MANDATORY):\n"
    "- The explanation of the correct answer MUST match the selected correct letter\n"
    "- The correct answer text MUST exactly correspond to the explanation labeled as correct\n"
    "- NEVER mismatch explanation and answer letter\n\n"

    "DIVERSITY CONTROL:\n"
    "- Apply {DIVERSITY_MODE} within the subtopic\n"
    "- Do NOT break anatomical correctness\n"
    "- Avoid repeating structures from {RECENT_QUESTIONS}\n\n"

    "ANSWER CONSTRUCTION (STRICT ORDER):\n"
    "1. Define the correct answer\n"
    "2. Validate it is uniquely correct\n"
    "3. Generate 3 plausible distractors (same category)\n"
    "4. Randomize position but FORCE correct answer to {CORRECT_LETTER}\n"
    "5. Set correct_answer = {CORRECT_LETTER}\n\n"

    "EXPLANATIONS (STRICT):\n"
    "- Correct: explain specifically WHY it is correct (anatomy-based reasoning)\n"
    "- Incorrect: explain WHY it is incorrect (not just definition)\n"
    "- Each explanation MUST reference the structure in that option\n"
    "- NO generic phrases\n\n"

    "QUALITY FILTER (FINAL CHECK BEFORE OUTPUT):\n"
    "- Question matches SUB_TOPIC exactly\n"
    "- Only one correct answer exists\n"
    "- No duplicated or equivalent options\n"
    "- No conceptual errors\n"
    "- No mismatch between answers and explanations\n"
    "- Output is valid JSON\n\n"

    "LANGUAGE:\n"
    "- Rioplatense Spanish\n"
    "- Concise academic tone\n\n"

    "OUTPUT RULES (CRITICAL):\n"
    "- ALWAYS return valid JSON\n"
    "- NEVER include placeholders like {TOPIC}\n"
    "- NEVER include meta explanations or errors\n"
    "- NEVER leave fields empty\n\n"

    "{\n"
    "\"question\": \"...\",\n"
    "\"answer_a\": \"...\",\n"
    "\"answer_b\": \"...\",\n"
    "\"answer_c\": \"...\",\n"
    "\"answer_d\": \"...\",\n"
    "\"explanation_a\": \"...\",\n"
    "\"explanation_b\": \"...\",\n"
    "\"explanation_c\": \"...\",\n"
    "\"explanation_d\": \"...\",\n"
    "\"correct_answer\": \"A|B|C|D\"\n"
    "}"
)
