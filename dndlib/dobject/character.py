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
    }

    def __init__(self, **kwargs):
        pass
