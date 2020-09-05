from pynd.dobject.dobject import Dobject


class Spell(Dobject):
    CONFIG = {

    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
