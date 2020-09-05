from pynd.dobject.dobject import Dobject

from pynd.dice.dice import *


class Character(Dobject):
    CONFIG = {
        "Playable": False,
        "Race": None,
        "Class": None,
        "Name": None,
        "Age": None,
        "Height": None,
        "Weight": None,
        "Gender": None,
        "Level": 1,
        "Experience": 0,
        "HP": None,
        "CA": None,
        "Abilities": {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0,
        },
        # TODO: test if I can overwrite those
        "Language": {
            "Standard": {
                "Common": False,
                "Dwarvish": False,
                "Elvish": False,
                "Giant": False,
                "Gnomish": False,
                "Goblin": False,
                "Hafling": False,
                "Orc": False,
            },
            "Exotic": {
                "Abyssal": False,
                "Celestial": False,
                "Deep Speech": False,
                "Draconic": False,
                "Infernal": False,
                "Primordial": False,
                "Sylvan": False,
                "Undercommon": False,
            },
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Set default method

    def set_default_all(self):
        self.set_default_to_class()
        self.set_default_to_race()

    def set_default_to_race(self):
        self.set_default_language_to_race()
        self.set_default_height_to_race()
        self.set_default_weight_to_race()

    def set_default_to_class(self):
        self.set_default_abilities()

    def set_default_language_to_race(self):
        pass

    def set_default_height_to_race(self):
        pass

    def set_default_weight_to_race(self):
        pass

    def set_default_abilities(self):
        pass


class PlayableCharacter(Character):
    CONFIG = {
        "Playable": True,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
