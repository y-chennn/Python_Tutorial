import random 

MAX = 5
MIN = 0

def more_or_less(a, b):
    c = a if a > b else b
    return c

def guest_number(num:int):
    target = random.randint(MIN, MAX)
    if num < 0 or num > 50:
        return print('number need in range(0, 5)')
    else:
        if num < target:
            print('less')
        elif num > target:
            print('more')
        else:
            print('congratulate')

if __name__ == '__main__':
    a, b = 1, 5
    print(more_or_less(a, b))
    
    # num = int(input('please enter a number: '))
    # guest_number(num)

    