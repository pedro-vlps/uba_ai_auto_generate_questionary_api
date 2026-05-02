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
    "innervation_or_vascularization",
    "exception"
]

LOCOMOTOR_DESCRIPTIONS = {
    "osteologia_general": "estructura, tipos de huesos, osificación, irrigación e inervación ósea",
    "osteologia_miembro_superior": "huesos del miembro superior, accidentes óseos y relaciones",
    "osteologia_miembro_inferior": "huesos del miembro inferior, relieves y funciones",
    "osteologia_columna_vertebral": "vértebras, características regionales y articulación",
    "osteologia_torax": "esternón, costillas y su organización estructural",
    "osteologia_craneo": "huesos del cráneo, base y bóveda, forámenes",

    "articulaciones_general": "tipos articulares, movimientos y estructuras asociadas",
    "articulaciones_miembro_superior": "articulaciones del miembro superior y sus movimientos",
    "articulaciones_miembro_inferior": "articulaciones del miembro inferior",
    "articulaciones_columna": "articulaciones vertebrales y discos intervertebrales",
    "articulaciones_craneo": "suturas y articulaciones craneales",

    "miologia_general": "tipos musculares, inserciones, irrigación e inervación",
    "musculos_miembro_superior": "músculos del miembro superior y sus funciones",
    "musculos_miembro_inferior": "músculos del miembro inferior",
    "musculos_espalda": "músculos superficiales y profundos del dorso",
    "musculos_torax": "músculos intercostales y respiratorios",
    "musculos_cabeza": "músculos faciales y masticadores",
    "musculos_cuello": "músculos cervicales y sus funciones",

    "compartimentos_brazo": "compartimentos anterior y posterior del brazo",
    "compartimentos_antebrazo": "compartimentos flexor y extensor",
    "compartimentos_mano": "compartimentos musculares de la mano",
    "compartimentos_muslo": "compartimentos del muslo",
    "compartimentos_pierna": "compartimentos de la pierna",
    "compartimentos_pie": "compartimentos del pie",

    "arterias_miembro_superior": "irrigación arterial del miembro superior",
    "arterias_miembro_inferior": "irrigación arterial del miembro inferior",
    "venas_miembro_superior": "drenaje venoso superficial y profundo superior",
    "venas_miembro_inferior": "drenaje venoso del miembro inferior",

    "plexo_braquial": "formación, ramos y territorios del plexo braquial",
    "plexo_lumbar": "nervios del plexo lumbar",
    "plexo_sacro": "formación y ramas del plexo sacro",
    "nervios_miembro_superior": "inervación periférica del miembro superior",
    "nervios_miembro_inferior": "inervación del miembro inferior",

    "axila": "límites, contenido y relaciones de la axila",
    "region_deltoidea": "estructura y contenido de la región deltoidea",
    "fosa_cubital": "límites y contenido de la fosa cubital",
    "canal_carpiano": "contenido y límites del túnel carpiano",
    "triangulo_femoral": "límites y contenido del triángulo femoral",
    "conducto_aductor": "trayecto y contenido del conducto aductor",
    "fosa_poplitea": "límites y contenido de la fosa poplítea",

    "regiones_topograficas_cabeza": "división anatómica superficial de la cabeza",
    "regiones_topograficas_cuello": "triángulos cervicales y contenido",
    "regiones_topograficas_tronco": "regiones del tronco y referencias anatómicas",
    "regiones_topograficas_miembro_superior": "regiones superficiales del miembro superior",
    "regiones_topograficas_miembro_inferior": "regiones del miembro inferior",

    "linfaticos_miembro_superior": "drenaje linfático del miembro superior",
    "linfaticos_miembro_inferior": "drenaje linfático del miembro inferior",
    "linfaticos_dorso": "linfáticos del dorso",
    "linfaticos_nuca": "drenaje linfático de la región nucal"
}

SPLACHNOLOGY_DESCRIPTIONS = {
    "cavidad_oral": "estructura, límites y contenido de la cavidad oral",
    "lengua": "músculos, inervación y vascularización de la lengua",
    "glandulas_salivales": "glándulas mayores y menores, drenaje y función",
    "faringe": "divisiones, músculos e irrigación",
    "esofago": "trayecto, capas y relaciones",
    "estomago": "regiones, irrigación e inervación",
    "intestino_delgado": "duodeno, yeyuno e íleon",
    "intestino_grueso": "colon, ciego y recto",
    "higado": "segmentación, irrigación y drenaje",
    "vias_biliares": "conductos biliares y drenaje",
    "vesicula_biliar": "estructura e irrigación",
    "pancreas": "regiones, función e irrigación",

    "cavidad_nasal": "estructura y límites",
    "senos_paranasales": "tipos y drenaje",
    "laringe": "cartílagos, músculos e inervación",
    "traquea": "estructura y relaciones",
    "bronquios": "división bronquial",
    "pulmones": "lóbulos y segmentación",
    "pleura": "hojas pleurales y cavidad",

    "rinon": "estructura, nefrona e irrigación",
    "ureter": "trayecto y estrechamientos",
    "vejiga": "estructura y relaciones",
    "uretra": "porciones y diferencias sexuales",

    "testiculo": "estructura y función",
    "epididimo": "maduración espermática",
    "conducto_deferente": "trayecto y función",
    "vesiculas_seminais": "secreción seminal",
    "prostata": "estructura e irrigación",
    "pene": "estructura y vascularización",

    "ovario": "estructura y función",
    "trompas_uterinas": "segmentos y función",
    "utero": "estructura y capas",
    "vagina": "estructura y relaciones",
    "genitales_externos_femeninos": "vulva y componentes",

    "peritoneo": "hojas y cavidad peritoneal",
    "mesenterios": "fijación de vísceras",
    "epiplones": "omento mayor y menor",
    "retroperitoneo": "órganos retroperitoneales",

    "linfatico_abdominal": "drenaje linfático abdominal",
    "linfatico_toracico": "linfáticos torácicos",
    "conducto_toracico": "trayecto y drenaje",
    "ganglios_linfaticos_abdominales": "grupos ganglionares abdominales",
    "ganglios_linfaticos_toracicos": "ganglios torácicos",

    "peritoneo_fascia_coalescencia": "fascias de coalescencia y fijación",

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

    "musculos_abdomen": "músculos de la pared abdominal",
    "musculatura_abdominal": "función y organización muscular abdominal",
    "musculatura_respiratoria": "músculos respiratorios",
    "musculatura_pelvica": "suelo pélvico"
}

NEURO_DESCRIPTIONS = {
    "medula_espinal": "segmentos, sustancia gris y blanca",
    "tronco_encefalico": "mesencéfalo, puente y bulbo",
    "bulbo_raquideo": "núcleos y funciones",
    "puente": "estructura y conexiones",
    "mesencefalo": "pedúnculos y colículos",

    "cerebelo": "lóbulos y funciones motoras",
    "diencefalo": "tálamo e hipotálamo",
    "talamus": "núcleos y funciones",
    "hipotalamo": "control autonómico",

    "telencefalo": "hemisferios cerebrales",
    "corteza_cerebral": "áreas funcionales",
    "lobulos_cerebrales": "división cortical",
    "ganglios_basales": "núcleos profundos",

    "vias_motoras": "vías descendentes",
    "vias_piramidales": "tracto corticoespinal",
    "vias_extrapiramidales": "control motor involuntario",
    "vias_sensitivas": "vías ascendentes",

    "nervios_craneales": "pares craneales y funciones",
    "nervio_olfatorio": "olfacción",
    "nervio_optico": "visión",
    "nervio_oculomotor": "movimientos oculares",
    "nervio_troclear": "músculo oblicuo superior",
    "nervio_trigemino": "sensibilidad facial",
    "nervio_abducens": "músculo recto lateral",
    "nervio_facial": "expresión facial",
    "nervio_vestibulococlear": "audición y equilibrio",
    "nervio_glosofaringeo": "deglución y gusto",
    "nervio_vago": "inervación parasimpática",
    "nervio_accesorio": "inervación de ECM y trapecio",
    "nervio_hipogloso": "movimiento lingual",

    "sistema_nervioso_autonomo": "simpático y parasimpático",
    "simpatico": "respuestas de alerta",
    "parasimpatico": "funciones viscerales",

    "meninges": "duramadre, aracnoides y piamadre",
    "liquido_cefalorraquideo": "producción y circulación",
    "ventriculos_cerebrales": "sistema ventricular",

    "irrigacion_cerebral": "arterias cerebrales",
    "circulo_de_willis": "anastomosis arterial",
    "senos_venosos": "drenaje venoso dural",

    "ojo": "estructura ocular",
    "oido": "oído externo, medio e interno",
    "vias_opticas": "trayecto visual",
    "vias_auditivas": "trayecto auditivo",

    "drenaje_venoso_superficial_cerebral": "venas superficiales",
    "drenaje_venoso_profundo_cerebral": "sistema venoso profundo",

    "drenaje_linfatico_cerebral": "drenaje linfático encefálico",

    "sistema_vertebrobasilar": "arterias vertebrales y basilar",

    "irrigacion_cerebral_detallada": "ramas arteriales cerebrales detalladas"
}

ANATOMY_QUESTION = (
    "You are a senior medical professor specialized in Human Anatomy and an expert "
    "in designing multiple-choice questions that STRICTLY follow the style of UBA exams. "

    "TASK:"
    "Generate EXACTLY ONE multiple-choice question."

    "TOPIC:"
    "{TOPIC}"

    "SUB TOPIC:"
    "{SUB_TOPIC}"

    "SUB TOPIC DESCRIPTION:"
    "{SUBTOPIC_DESCRIPTION}"

    "DIVERSITY MODE:"
    "{DIVERSITY_MODE}"

    "ANTI-REPETITION:"
    "Avoid similarity with:"
    "{RECENT_QUESTIONS}"

    "CORE REQUIREMENTS:"
    "- The question MUST be SHORT and DIRECT"
    "- The question MUST test ONE concept"
    "- DO NOT use clinical cases"
    "- DO NOT add unnecessary context"

    "DOMAIN ENFORCEMENT (CRITICAL):"
    "- The question MUST be strictly about {SUB_TOPIC}"
    "- Use ONLY structures related to this subtopic"
    "- DO NOT include structures from other systems"
    "- All answer options MUST belong to the same anatomical category"

    "DIVERSITY CONTROL:"
    "- Apply {DIVERSITY_MODE} only within the subtopic context"
    "- It must NOT override anatomical correctness"

    "ANSWER CONTROL (STEP BY STEP):"
    "1. Determine the correct answer"
    "2. Ensure it is uniquely correct"
    "3. Create 3 plausible but incorrect alternatives"
    "4. Place the correct answer in {CORRECT_LETTER}"
    "5. Mark 'correct_answer' as {CORRECT_LETTER}"

    "LANGUAGE:"
    "- Rioplatense Spanish"
    "- Concise academic tone"

    "OUTPUT:"
    "Return ONLY valid JSON"

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
    "}"
)
