import numpy as np

from pynd.constants import *
from pynd.dobject.dobject import Dobject
from pynd.dobject.item import Item

from pynd.utils.config_ops import digest_config


class Coin(Item):
    CONFIG = {
        "name": "Coin",
        "consumable": True,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CopperCoin(Coin):
    CONFIG = {
        "name": "cp",
        "value": CP,
    }
    pass


class SilverCoin(Coin):
    CONFIG = {
        "name": "sp",
        "value": SP,
    }
    # 1sp = 10cp
    pass


class ElectrumCoin(Coin):
    CONFIG = {
        "name": "ep",
        "value": EP
    }
    # 1ep = 5sp
    pass


class GoldCoin(Coin):
    CONFIG = {
        "name": "gp",
        "value": GP,
    }
    # 1gp = 2ep
    pass


class PlatinumCoin(Coin):
    CONFIG = {
        "name": "pp",
        "value": PP,
    }
    # 1pp = 10 gb
    pass
