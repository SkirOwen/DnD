from pynd.dobject.dobject import Dobject


class Weapon(Dobject):
    CONFIG = {

    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
