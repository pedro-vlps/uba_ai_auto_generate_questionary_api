import random

from src.helpers.questions_text import LOCOMOTOR, SPLACHNOLOGY, NEUROANATOMY

def check_anatomy_sub_topic(parameter):
    if parameter == 'Locomotor':
        return random.choice(LOCOMOTOR)

    if parameter == 'Neuroanatomy':
        return random.choice(NEUROANATOMY)

    if parameter == 'Splanchnology':
        return random.choice(SPLACHNOLOGY)
