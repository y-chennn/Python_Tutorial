import numpy as np


class character:
    def __init__(self, name, race, char_class) -> None:
        self.__name = name
        self.__race = race
        self.__char_class = char_class

        self.__BASIC_ABILITY = {
            "STR": 50,  # strength
            "DEX": 50,  # dexterity
            "INT": 50,  # intelligence
            # "CON": 100,  # constitution
            # "HP": 100,  # hit points
        }

        self.__ability = self._assign_ability(self.__BASIC_ABILITY)

    def _assign_ability(self, ability: dict):
        ability = self._cal_race_bonus(list(ability.values()), self.__race)
        ability = self._cal_class_bonus(ability, self.__char_class)
        ability_dict = dict(
            {
                "STR": ability[0],  # strength
                "DEX": ability[1],  # dexterity
                "INT": ability[2],  # intelligence
            }
        )
        return ability_dict

    @classmethod
    def _cal_race_bonus(cls, ability, race) -> list:
        if race == "人類":
            ability = list(ability)
        elif race == "矮人":
            ability = list(np.add(ability, [20, 0, -20]))
        elif race == "精靈":
            ability = list(np.add(ability, [-20, 0, 20]))

        return ability

    @classmethod
    def _cal_class_bonus(cls, ability, char_class) -> list:
        if char_class == "戰士":
            ability = list(np.multiply(ability, [1.3, 1, 0.9]))
        elif char_class == "遊俠":
            ability = list(np.multiply(ability, [0.9, 1.3, 1]))
        elif char_class == "法師":
            ability = list(np.multiply(ability, [0.9, 1, 1.3]))

        return ability

    def rename(self, name):
        self.__name = name

    def change_class(self, char_class):
        self.__char_class = char_class
        self.__ability = self._assign_ability(self.__BASIC_ABILITY)

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_char_class(self):
        return self.__char_class

    def get_ability(self):
        return self.__ability


if __name__ == "__main__":
    role = character("123", "人類", "戰士")
    print(role.get_name())
    print(role.get_race())
    print(role.get_char_class())
    print(role.get_ability())
    role.change_class("法師")
    print(role.get_char_class())
    print(role.get_ability())
