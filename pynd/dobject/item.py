from pynd.dobject.dobject import Dobject
import pynd.dobject.coin as coin


class Item(Dobject):
    CONFIG = {
        "consumable": False,
        "cost": (0, None),
        "weight": 0,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Maybe do a file for that?
# Yeah maybe indeed
class Ammunition(Item):
    CONFIG = {
        "cost": (0, None),
        "consumable": True,
        "amount": 20,
        "weight": 0,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def use(self, ammo_current, ammo_used):
    #     ammo_current -= ammo_used
    #     return ammo_current

# TODO: redo this in the Ammunition class, and figure out the kwargs
class Arrow(Ammunition):
    CONFIG = {
        "default_cost": (1, coin.GoldCoin),
        "default_amount": 20,
        "default_weight": 1,
    }

    def __init__(self, **kwargs):
        Ammunition.__init__(self, **kwargs)
        self.cost = self.default_cost
        self.amount = self.default_amount
        self.weight = self.default_weight

        self.cost_per_ammo = self.default_cost / self.default_amout
        self.weight_per_ammo = self.default_weight / self.default_amount

    def update(self, ammo_win_lose):
        self.amount += ammo_win_lose
        self.update_cost(ammo_win_lose)
        self.update_weight(ammo_win_lose)
        return self

    def use(self, ammo_used):
        self.update(-ammo_used)
        return self

    def gain(self, ammo_gained):
        self.update(ammo_gained)
        return self

    def update_cost(self, ammo_used):
        self.cost += self.cost_per_ammo * ammo_used
        return self

    def update_weight(self, ammo_used):
        self.weight += self.weight_per_ammo * ammo_used
