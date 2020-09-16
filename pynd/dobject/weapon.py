from pynd.dobject.dobject import Dobject


class Weapon(Dobject):
    CONFIG = {
        "use_ammo": False,
        "ranged": False,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Sword(Weapon):
    CONFIG = {
    }

    def __init__(self, weapon, **kwargs):
        Weapon.__init__(self, **kwargs)


class Bow(Weapon):
    CONFIG = {
        "use_ammo": True,
        "ranged": True,
        "ammo_type": None,
    }

    def __init__(self, weapon, **kwargs):
        Weapon.__init__(self, **kwargs)
