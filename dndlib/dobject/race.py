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

# DISCLAIMER
# Race is not well defined in biology whereas species is.
# In the context of DnD race is more appropriate, unless someone
# wants to classify everything according to modern taxonomy. Have fun!


class race(Dobject):
    def __init__(self):
        pass
