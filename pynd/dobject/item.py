from pynd.dobject.dobject import Dobject


class Item(Dobject):
    CONFIG = {
        "consumable": False,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Maybe do a file for that?
class Ammunition(Item):
    CONFIG = {
        "consumable": True,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, ammo_current, ammo_used):
        ammo_current -= ammo_used
        return ammo_current
