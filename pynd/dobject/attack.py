from pynd.dobject.dobject import Dobject
from pynd.dice.dice import *
from pynd.dobject.weapon import *
from pynd.dobject.spell import *
from pynd.dobject.item import *


class Attack(Dobject):
    CONFIG = {
        "heavy": False,

    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.heavy:
            pass
