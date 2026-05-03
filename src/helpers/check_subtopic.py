import random

from src.helpers.questions_text import (
    LOCOMOTOR_DESCRIPTIONS,
    SPLACHNOLOGY_DESCRIPTIONS,
    NEURO_DESCRIPTIONS,
)


def check_anatomy_sub_topic(parameter):
    if parameter == "Locomotor":
        key = random.choice(list(LOCOMOTOR_DESCRIPTIONS.keys()))
        return [key, LOCOMOTOR_DESCRIPTIONS[key]]

    if parameter == "Neuroanatomy":
        key = random.choice(list(NEURO_DESCRIPTIONS.keys()))
        return [key, NEURO_DESCRIPTIONS[key]]

    if parameter == "Splanchnology":
        key = random.choice(list(SPLACHNOLOGY_DESCRIPTIONS.keys()))
        return [key, SPLACHNOLOGY_DESCRIPTIONS[key]]

    raise ValueError(f"Unsupported anatomy topic: {parameter}")
