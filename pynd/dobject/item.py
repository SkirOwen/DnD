from pynd.dobject.dobject import Dobject


class Item(Dobject):
    CONFIG = {
        "Consumable": False,
    }

    def __init__(self, **kwargs):
        pass


class Ammunition(Item):
    CONFIG = {
        "Consumable": True,
    }

    def __init__(self, **kwargs):
        pass

    def use(self, ammo_left, ammo_used):
        ammo_left -= ammo_used
        return ammo_left
