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

LOCOMOTOR = [
    # Osteología
    "osteologia_general",
    "osteologia_miembro_superior",
    "osteologia_miembro_inferior",
    "osteologia_columna_vertebral",
    "osteologia_torax",
    "osteologia_craneo",

    # Artrología
    "articulaciones_general",
    "articulaciones_miembro_superior",
    "articulaciones_miembro_inferior",
    "articulaciones_columna",
    "articulaciones_craneo",

    # Miología
    "miologia_general",
    "musculos_miembro_superior",
    "musculos_miembro_inferior",
    "musculos_espalda",
    "musculos_torax",
    "musculos_cabeza",
    "musculos_cuello",

    # Compartimentos / regiones
    "compartimentos_brazo",
    "compartimentos_antebrazo",
    "compartimentos_mano",
    "compartimentos_muslo",
    "compartimentos_pierna",
    "compartimentos_pie",

    # Vasos locomotor
    "arterias_miembro_superior",
    "arterias_miembro_inferior",
    "venas_miembro_superior",
    "venas_miembro_inferior",

    # Nervios periféricos
    "plexo_braquial",
    "plexo_lumbar",
    "plexo_sacro",
    "nervios_miembro_superior",
    "nervios_miembro_inferior",

    # Anatomía regional
    "axila",
    "region_deltoidea",
    "fosa_cubital",
    "canal_carpiano",
    "triangulo_femoral",
    "conducto_aductor",
    "fosa_poplitea"

    # Regiões topográficas
    "regiones_topograficas_cabeza",
    "regiones_topograficas_cuello",
    "regiones_topograficas_tronco",
    "regiones_topograficas_miembro_superior",
    "regiones_topograficas_miembro_inferior",

    # Sistema linfático locomotor
    "linfaticos_miembro_superior",
    "linfaticos_miembro_inferior",
    "linfaticos_dorso",
    "linfaticos_nuca"
]

SPLACHNOLOGY = [
    # Sistema digestivo
    "cavidad_oral",
    "lengua",
    "glandulas_salivales",
    "faringe",
    "esofago",
    "estomago",
    "intestino_delgado",
    "intestino_grueso",
    "higado",
    "vias_biliares",
    "vesicula_biliar",
    "pancreas",

    # Sistema respiratorio
    "cavidad_nasal",
    "senos_paranasales",
    "laringe",
    "traquea",
    "bronquios",
    "pulmones",
    "pleura",

    # Sistema urinario
    "rinon",
    "ureter",
    "vejiga",
    "uretra",

    # Sistema reproductor masculino
    "testiculo",
    "epididimo",
    "conducto_deferente",
    "vesiculas_seminais",
    "prostata",
    "pene",

    # Sistema reproductor femenino
    "ovario",
    "trompas_uterinas",
    "utero",
    "vagina",
    "genitales_externos_femeninos",

    # Peritoneo y cavidad
    "peritoneo",
    "mesenterios",
    "epiplones",
    "retroperitoneo",

    # Sistema linfático (IMPORTANTÍSIMO)
    "linfatico_abdominal",
    "linfatico_toracico",
    "conducto_toracico",
    "ganglios_linfaticos_abdominales",
    "ganglios_linfaticos_toracicos"

    # Peritoneo específico
    "peritoneo_fascia_coalescencia",

    # Linfáticos
    "linfaticos_cabeza_cuello",
    "linfaticos_pelvicos",
    "linfaticos_abdominales_detallados",
    "linfaticos_toracicos_detallados",

    # Drenaje venoso (antes seria tag)
    "drenaje_venoso_superficial_abdominal",
    "drenaje_venoso_profundo_abdominal",
    "drenaje_venoso_superficial_pelvico",
    "drenaje_venoso_profundo_pelvico",

    # Irrigación (granularizada)
    "irrigacion_digestivo",
    "irrigacion_respiratorio",
    "irrigacion_pelvico",

    # Miologia visceral (importante e faltante)
    "musculos_abdomen",
    "musculatura_abdominal",
    "musculatura_respiratoria",
    "musculatura_pelvica"
]

NEUROANATOMY = [
    # Sistema nervioso central
    "medula_espinal",
    "tronco_encefalico",
    "bulbo_raquideo",
    "puente",
    "mesencefalo",

    "cerebelo",
    "diencefalo",
    "talamus",
    "hipotalamo",

    "telencefalo",
    "corteza_cerebral",
    "lobulos_cerebrales",
    "ganglios_basales",

    # Vías
    "vias_motoras",
    "vias_piramidales",
    "vias_extrapiramidales",
    "vias_sensitivas",

    # Nervios craneales
    "nervios_craneales",
    "nervio_olfatorio",
    "nervio_optico",
    "nervio_oculomotor",
    "nervio_troclear",
    "nervio_trigemino",
    "nervio_abducens",
    "nervio_facial",
    "nervio_vestibulococlear",
    "nervio_glosofaringeo",
    "nervio_vago",
    "nervio_accesorio",
    "nervio_hipogloso",

    # Sistema autónomo
    "sistema_nervioso_autonomo",
    "simpatico",
    "parasimpatico",

    # Meninges y LCR
    "meninges",
    "liquido_cefalorraquideo",
    "ventriculos_cerebrales",

    # Vascularización
    "irrigacion_cerebral",
    "circulo_de_willis",
    "senos_venosos",

    # Órganos de los sentidos
    "ojo",
    "oido",
    "vias_opticas",
    "vias_auditivas"

    # Drenaje venoso cerebral (MUITO IMPORTANTE)
    "drenaje_venoso_superficial_cerebral",
    "drenaje_venoso_profundo_cerebral",

    # Linfático (adaptado para subtópico)
    "drenaje_linfatico_cerebral",

    # Sistema arterial específico (faltante real)
    "sistema_vertebrobasilar",

    # Complemento importante (opcional mas recomendado)
    "irrigacion_cerebral_detallada"
]

ANATOMY_QUESTION = (
    "You are a senior medical professor specialized in Human Anatomy and an expert "
    "in designing multiple-choice questions that STRICTLY follow the style of UBA exams. "

    "TASK:"
    "Generate EXACTLY ONE multiple-choice question."

    "SOURCE CONSTRAINT:"
    "Base the question strictly on the following references:"
    "- Anatomía Humana, Latarjet & Ruiz Liard "
    "- Netter Atlas of Human Anatomy "
    "- Rouvière & Delmas "
    "- Pró "

    "TOPIC:"
    "{TOPIC}"

    "SUB TOPIC:"
    "{SUB_TOPIC}"

    "DIVERSITY MODE:"
    "{DIVERSITY_MODE}"

    "ANTI-REPETITION:"
    "Avoid similarity with:"
    "{RECENT_QUESTIONS}"

    "ANSWER CONTROL (CRITICAL - FOLLOW STEP BY STEP):"
    "STEP 1: Internally determine the correct answer content"
    "STEP 2: Validate that this answer is uniquely correct"
    "STEP 3: Create three incorrect alternatives that are plausible but definitively wrong"
    "STEP 4: Place the correct answer content ONLY in option {CORRECT_LETTER}"
    "STEP 5: Ensure all other options are incorrect"
    "STEP 6: Set 'correct_answer' field to {CORRECT_LETTER}"

    "STRICT RULES:"
    "- The content of option {CORRECT_LETTER} MUST be correct"
    "- The correct answer MUST NOT appear in any other option"
    "- Do NOT relabel options after creation"
    "- Do NOT assign correctness without verifying content"

    "UNIQUE CORRECT ANSWER (CRITICAL):"
    "- There MUST be exactly ONE correct answer"
    "- All other options MUST be clearly incorrect when compared to the correct one"
    "- Incorrect options must not be partially correct or context-dependent"
    "- Avoid answers that could be interpreted as correct under any circumstance"
    "- If more than one option could be correct, you MUST internally fix the question before output"
    "- Ensure exclusivity: only one option satisfies the question fully"

    "CRITICAL STYLE REQUIREMENTS (UBA FORMAT):"
    "- The question MUST be SHORT and DIRECT"
    "- The question MUST test ONE specific concept"
    "- DO NOT use clinical cases or patient scenarios"
    "- DO NOT include unnecessary context"
    "- DO NOT include clues that make the answer obvious"
    "- The question should resemble real exam statements"

    "COHERENCE RULE (VERY IMPORTANT):"
    "- All answer options MUST belong to the SAME category"
    "  (e.g., all nerves, all arteries, all muscles)"
    "- DO NOT mix anatomical systems or unrelated regions"
    "- The question MUST stay strictly within the given TOPIC and SUB TOPIC"

    "COGNITIVE LEVEL:"
    "- Focus on recognition and conceptual distinction"
    "- Avoid multi-step reasoning"
    "- Avoid overly complex logic"

    "DISTRACTOR RULES:"
    "- All incorrect options must be plausible BUT clearly "
    "incorrect upon precise anatomical knowledge"
    "- Distractors must be close to the correct concept but contain a specific error"
    "- Each incorrect option must fail for a different reason"
    "- Avoid generic or overlapping answers"
    "- Alternatives must be similar in structure and length"
    "- Avoid extreme or obviously incorrect answers"
    "- Avoid hints in wording, length, or specificity"

    "LANGUAGE:"
    "- Rioplatense Spanish"
    "- Use formal academic tone"
    "- Keep wording concise"

    "OUTPUT RULES (STRICT):"
    "- Return ONLY valid JSON"
    "- No extra text"
    "- No comments"
    "- No trailing commas"

    "JSON STRUCTURE:"
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

    "FINAL VALIDATION (MANDATORY):"
    "1. Question is short and direct"
    "2. No clinical scenario is present"
    "3. Only ONE concept is tested"
    "4. All options belong to same category"
    "5. The content of option {CORRECT_LETTER} is correct"
    "6. The 'correct_answer' field equals {CORRECT_LETTER}"
    "7. NO other option is correct under any interpretation"
    "8. Each incorrect option has a clear and identifiable error"
    "9. No obvious clues are present"
    "10. Matches UBA exam style"
)
