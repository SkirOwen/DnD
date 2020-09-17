from pynd.constants import *

from pynd.dobject.dobject import Dobject
import pynd.dobject.coin as coin


class Armour(Dobject):
    CONFIG = {
        "cost": (0, None),
        "armour_cat": None,
        "ac": 0,
        "modifier": (None, 0),
        "strength": None,
        "stealth_disadvantage": False,
        "weight": 0,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Light Armour


class PaddedArmour(Armour):
    CONFIG = {
        "cost": (5, coin.GoldCoin),
        "armour_cat": "Light_Armour",
        "ac": 11,
        "modifier": (Dex, 0),
        "stealth_disadvantage": True,
        "weight": 8,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class LeatherArmour(Armour):
    CONFIG = {
        "cost": (10, coin.GoldCoin),
        "armour_cat": "Light_Armour",
        "ac": 11,
        "modifier": (Dex, 0),
        "weight": 10,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class StuddedLeatherArmour(Armour):
    CONFIG = {
        "cost": (45, coin.GoldCoin),
        "armour_cat": "Light_Armour",
        "ac": 12,
        "modifier": (Dex, 0),
        "weight": 13,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


# Medium Armour


class HideArmour(Armour):
    CONFIG = {
        "cost": (10, coin.GoldCoin),
        "armour_cat": "Medium_Armour",
        "ac": 12,
        "modifier": (Dex, 2),
        "weight": 12,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class ChainShirtArmour(Armour):
    CONFIG = {
        "cost": (50, coin.GoldCoin),
        "armour_cat": "Medium_Armour",
        "ac": 13,
        "modifier": (Dex, 2),
        "weight": 20,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class ScaleMailArmour(Armour):
    CONFIG = {
        "cost": (50, coin.GoldCoin),
        "armour_cat": "Medium_Armour",
        "ac": 14,
        "modifier": (Dex, 2),
        "stealth_disadvantage": True,
        "weight": 45,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class BreastplateArmour(Armour):
    CONFIG = {
        "cost": (400, coin.GoldCoin),
        "armour_cat": "Medium_Armour",
        "ac": 14,
        "modifier": (Dex, 2),
        "weight": 20,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class HalfPlate(Armour):
    CONFIG = {
        "cost": (750, coin.GoldCoin),
        "armour_cat": "Medium_Armour",
        "ac": 15,
        "modifier": (Dex, 2),
        "stealth_disadvantage": True,
        "weight": 40,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


# Heavy Armour


class RingMailArmour(Armour):
    CONFIG = {
        "cost": (30, coin.GoldCoin),
        "armour_cat": "Heavy_Armour",
        "ac": 14,
        "stealth_disadvantage": True,
        "weight": 40,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class ChainMailArmour(Armour):
    CONFIG = {
        "cost": (75, coin.GoldCoin),
        "armour_cat": "Heavy_Armour",
        "ac": 16,
        "strength": 13,
        "stealth_disadvantage": True,
        "weight": 55,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class SplintArmour(Armour):
    CONFIG = {
        "cost": (200, coin.GoldCoin),
        "armour_cat": "Heavy_Armour",
        "ac": 17,
        "strength": 15,
        "stealth_disadvantage": True,
        "weight": 60,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


class PlateArmour(Armour):
    CONFIG = {
        "cost": (1500, coin.GoldCoin),
        "armour_cat": "Heavy_Armour",
        "ac": 18,
        "strength": 15,
        "stealth_disadvantage": True,
        "weight": 65,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)


# Shield


class Shield(Armour):
    CONFIG = {
        "cost": (10, coin.GoldCoin),
        "armour_cat": "Shield",
        "ac": 2,
        "modifier": (None, 0),
        "weight": 6,
    }

    def __init__(self, **kwargs):
        Armour.__init__(self, **kwargs)
