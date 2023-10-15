import math
import random


def factorize(num: int) -> list:
    factor = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor.append(i)
    return factor


def raindrops(num: int):
    factor = factorize(num)
    sound = ""
    if 3 in factor:
        sound = sound + "pling"
    if 5 in factor:
        sound = sound + "plang"
    if 7 in factor:
        sound = sound + "plong"
    if len(sound) == 0:
        sound = "nothing"
    return sound


if __name__ == "__main__":
    # num = random.randint(0, 50)
    num = 37
    print(num, factorize(num))
    print(raindrops(num))
