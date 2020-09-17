from pynd.dobject.dobject import Dobject
import pynd.dobject.coin as coin


class Animals(Dobject):
    CONFIG = {
        "cost": (0, None),
        "speed": 0,
        "carrying_capacity": 0,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
