from numpy.random import randint


class Die(object):
    # lagged_start as option to see each roll appear one
    # after the other?
    def __init__(self, D=6, roll_nbr=1):
        self.D = D
        self.roll_nbr = roll_nbr

    def rolling(self):
        result = []
        for roll in range(self.roll_nbr):
            result.append(randint(1, self.D + 1))
        return result

# Maybe too complicated
# But maybe nice to have a object for that?


class Dice(Die):
    def __init__(self, *dice, **kwargs):
        if not all([isinstance(d, Die) for d in dice]):
            raise Exception("All subdice must be of type Die")
        Die.__init__(self, **kwargs)
        self.add(*dice)
#     def __str__(self, *dice, **kwargs):
#         if not all([isinstance(d, Die) for d in dice]):
#             raise Exception("All dice must be of type Die")
#         Die.__init__(self, **kwargs)
#
#     def multi_roll(self):
#         result = []
#         for die in range(len(self.dice)):
#             Die.rolling()
