from pynd.dobject.dobject import Dobject


class Item(Dobject):
    CONFIG = {
        "Consumable": False,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Ammunition(Item):
    CONFIG = {
        "Consumable": True,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, ammo_current, ammo_used):
        ammo_current -= ammo_used
        return ammo_current
