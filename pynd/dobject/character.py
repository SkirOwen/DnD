from pynd.constants import *

from pynd.dobject.dobject import Dobject

from pynd.dice.dice import *


class Character(Dobject):
    CONFIG = {
        "playable": False,
        "player_name": None,
        "race": None,
        "class": None,
        "name": None,
        "age": None,
        "height": None,
        "weight": None,
        "gender": None,
        "level": 1,
        "experience": 0,
        "unconscious": False,
        "hp": None,
        "ac": None,
        "proficiency_bonus": 0,
        "abilities": {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
        },
        "perception": 0,
        "coins": {
            "copper": 0,
            "silver": 0,
            "electrum": 0,
            "gold" : 0,
            "platinum": 0,
        },
        # TODO: test if I can overwrite those
        "language": {
            "standard": {
                "common": False,
                "dwarvish": False,
                "elvish": False,
                "giant": False,
                "gnomish": False,
                "goblin": False,
                "hafling": False,
                "orc": False,
            },
            "exotic": {
                "abyssal": False,
                "celestial": False,
                "deep_speech": False,
                "draconic": False,
                "infernal": False,
                "primordial": False,
                "sylvan": False,
                "undercommon": False,
            },
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Leveling up and adding exp

    def get_experience(self, gained_experience):
        # TODO: adding exp after lvl 20, guess it is already here
        self.experience += gained_experience
        while self.level < 20 and self.check_level_up(self.experience):
            self.level_up()
        return self

    def check_level_up(self, new_exp):
        # TODO: What happen if exp_needed == current_exp?
        return LEVELING_TABLE[self.level] <= new_exp

    def level_up(self):
        self.level += 1
        return self

    # Damage and Healing

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.unconscious = True
        return self

    def heal(self, healing):
        self.hp += healing
        return self

    # Set default method

    def set_default_all(self):
        self.set_default_to_class()
        self.set_default_to_race()

    def set_default_to_race(self):
        self.set_default_language_to_race()
        self.set_default_height_to_race()
        self.set_default_weight_to_race()
        self.set_default_abilities_to_race()

    def set_default_to_class(self):
        self.set_default_abilities_to_class()

    def set_default_language_to_race(self):
        pass

    def set_default_height_to_race(self):
        pass

    def set_default_weight_to_race(self):
        pass

    def set_default_abilities_to_race(self):
        self.set_strength_to_race()
        self.set_dexterity_to_race()
        self.set_constitution_to_race()
        self.set_intelligence_to_race()
        self.set_wisdom_to_race()
        self.set_charisma_to_race()

    def set_strength_to_race(self):
        if self.race == "mountain_dwarf":
            pass

    def set_dexterity_to_race(self):
        pass

    def set_constitution_to_race(self):
        pass

    def set_intelligence_to_race(self):
        pass

    def set_wisdom_to_race(self):
        pass

    def set_charisma_to_race(self):
        pass

    def set_default_abilities_to_class(self):
        pass


class PlayableCharacter(Character):
    CONFIG = {
        "Playable": True,
    }

    def __init__(self, character, **kwargs):
        Character.__init__(self, **kwargs)
