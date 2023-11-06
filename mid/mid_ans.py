import numpy as np
import sys
import random


def create_role(name, race, career) -> dict:
    ability_base = [50, 50, 50]

    ability = create_race(ability_base, race)
    ability = create_career(ability, career)

    role = {
        "Id": name,
        "race": race,
        "class": career,
        "ability": dict(
            {
                "STR": ability[0],
                "DEX": ability[1],
                "INT": ability[2],
            }
        ),
    }
    return role


def create_race(ability, race) -> list:
    if race == "人類":
        ability = list(ability)
    elif race == "矮人":
        ability = list(np.add(ability, [20, 0, -20]))
    elif race == "精靈":
        ability = list(np.add(ability, [-20, 0, 20]))
    return ability


def create_career(ability, career) -> list:
    if career == "戰士":
        ability = list(np.multiply(ability, [1.3, 1, 0.9]))
    elif career == "遊俠":
        ability = list(np.multiply(ability, [0.9, 1.3, 1]))
    elif career == "法師":
        ability = list(np.multiply(ability, [0.9, 1, 1.3]))

    return ability


def roll_dice():
    return random.randint(1, 6)


def role_roll_dice(role: dict):
    # [1, 2, 3, 4, 5, 6]
    probability = [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]
    STR = role["ability"]["STR"]
    DEX = role["ability"]["DEX"]
    if STR > 50:
        probability[4] += probability[4] + (STR - 50) // 10 * 0.02
        probability[5] += probability[5] + (STR - 50) // 10 * 0.02
    elif STR < 50:
        probability[0] += probability[0] - (STR - 50) // 10 * 0.02
        probability[1] += probability[1] - (STR - 50) // 10 * 0.02

    if DEX > 50:
        probability[5] += probability[5] + (DEX - 50) // 10 * 0.02

    return random.choices(range(1, 7), probability)[0]


def generate_field():
    dice = roll_dice()
    if dice == 6:
        monster = 0
    elif dice in (2, 3, 4, 5):
        monster = 1
    else:
        monster = 2
    return (dice, monster)


def battle(role, num):
    def _battle():
        role_num = role_roll_dice(role)
        mon_num = role_roll_dice(role)

        print(f"    In battle, You roll {role_num}, the monster roll {mon_num}. ")

        if role_num > mon_num:
            return "win"
        elif role_num == mon_num:
            return _battle()
        else:
            return "lose"

    r = []
    for _ in range(0, num):
        r.append(_battle())
    return r


def adventure(role, times):
    step = 0
    streak = 0
    while step < times:
        field = generate_field()
        if field[0] == 6:
            print(f"Step {step+1}: Pass!")
            step += 1
        else:
            print(
                f"Step {step+1}: You roll a {field[0]}. You encounter {field[1]} monsters"
            )
            if battle(role, field[1]).count("lose") == 1:
                print("GAME OVER")
                break
            else:
                step += 1
                streak += 1
                if streak == 2:
                    print("YOU WIN")
                    break
    if step == 3:
        print("YOU WIN")


def dd_game():
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
    adventure(role, 3)


if __name__ == "__main__":
    dd_game()
