from functools import reduce
import copy
import itertools as it
import operator as op
import os
import random
import sys

from colour import Color
import numpy as np

import dndlib.constants as consts
from dndlib.constants import *
from dndlib.container.container import Container

from dndlib.dobject.dobject import Dobject


class Character(Dobject):
    CONFIG = {
        "Playable": False,
        "Race": None,
        "Class": None,
        "Name": None,
        "Age": None,
        "Gender": None,
        "Level": 1,
        "Experience": 0,
        "HP": None,
        "CA": None,
        "Abilities": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0,
        },
        # TODO: test if I can overwrite those
        "Language": {
            "Standard": {
                "Common": False,
                "Dwarvish": False,
                "Elvish": False,
                "Giant": False,
                "Gnomish": False,
                "Goblin": False,
                "Hafling": False,
                "Orc": False,
            },
            "Exotic": {
                "Abyssal": False,
                "Celestial": False,
                "Deep Speech": False,
                "Draconic": False,
                "Infernal": False,
                "Primordial": False,
                "Sylvan": False,
                "Undercommon": False,
            },
        },
    }

    def __init__(self, **kwargs):
        pass

    def set_language_default_to_race(self):
        pass
