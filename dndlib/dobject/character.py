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
    def __init__(self, **kwargs):
        Container.__init__(self, **kwargs)
