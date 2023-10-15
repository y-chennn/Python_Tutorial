import random

MAX = 10
MIN = 1

def gauss_number(x, ans):
    if x == ans:
        print(f'Good job, ans is {x}')
    elif x > ans:
        print('ur ans is bigger')
    elif x < ans:
        print('ur ans is smaller')
    else:
        print('out of range')

ans = random.randint(MIN, MAX)

# for i in range(0, 5):
#     num = int(input(f"please enter a number in {MIN} to {MAX}, u got {5-i} time(s) chance: "))
#     gauss_number(num, ans)

# i = 5
# while i > 0:
#     num = int(input(f"please enter a number in {MIN} to {MAX}, u got {i} time(s) chance: "))
#     gauss_number(num, ans)
#     i = i - 1