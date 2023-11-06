import numpy as np
import sys
import random


def create_role(name, race, career) -> dict:
    ability = create_race(race)
    role = {
        "Id": name,
        "race": race,
        "class": career,
        "ability": create_career(career, ability),
    }
    return role


def create_race(race) -> list:
    ability_base = [50, 50, 50]

    if race == "人類":
        ability = list(ability_base)
    elif race == "矮人":
        ability = list(np.add(ability_base, [20, 0, -20]))
    elif race == "精靈":
        ability = list(np.add(ability_base, [-20, 0, 20]))
    return ability


def create_career(career, ability) -> dict:
    if career == "戰士":
        ability = tuple(np.multiply(ability, [1.3, 1, 0.9]))
    elif career == "遊俠":
        ability = tuple(np.multiply(ability, [0.9, 1.3, 1]))
    elif career == "法師":
        ability = tuple(np.multiply(ability, [0.9, 1, 1.3]))

    ability_dict = dict(
        {
            "STR": ability[0],
            "DEX": ability[1],
            "INT": ability[2],
        }
    )
    return ability_dict


def roll_dice():
    return random.randint(1, 6)


def generate_field():
    dice = roll_dice()
    if dice == 6:
        monster = 0
    elif dice in (2, 3, 4, 5):
        monster = 1
    else:
        monster = 2
    return (dice, monster)


def battle():
    role_num = roll_dice()
    mon_num = roll_dice()

    print(f"    In battle, You roll {role_num}, the monster roll {mon_num}. ")

    if role_num > mon_num:
        return "win"
    elif role_num == mon_num:
        return battle()
    else:
        return "lose"


def combo_battle(num):
    r = []
    for i in range(0, num):
        r.append(battle())
    return r


def adventure(role, times):
    step = 0
    streak = 0
    while step < times and streak < 3:
        field = generate_field()
        if field[0] == 6:
            print(f"Step {step+1}: Pass!")
        else:
            print(
                f"Step {step+1}: You roll a {field[0]}. You encounter {field[1]} monsters"
            )
            if combo_battle(field[1]).count("lose") == 1:
                print("GAME OVER")
                break
            else:
                step += 1
                streak += 1

            if streak == 2:
                print("YOU WIN")

                break


if __name__ == "__main__":
    race_list = ("人類", "矮人", "精靈")
    class_list = ("戰士", "遊俠", "法師")

    name = input("請輸入姓名: ")
    race = input("請輸入種族('人類', '矮人', '精靈'): ")
    if race not in race_list:
        print("輸入錯誤")
        sys.exit()
    career = input("請輸入職業('戰士', '遊俠', '法師'): ")
    if career not in class_list:
        print("輸入錯誤")
        sys.exit()
    role = create_role(name, race, career)
    print(role)

    # role = {}
    # adventure(role, 3)
    # print(combo_battle(2))
