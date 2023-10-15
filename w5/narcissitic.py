import random


def is_narcissistic(num: int) -> bool:
    num_d = []
    d = len(str(num))
    for i in range(d):
        num_d.append(int(str(num)[i]))
    for n, i in enumerate(num_d):
        num_d[n] = i**d
    # num_d = [item**d for item in num_d]
    return num == sum(num_d)

    # d = len(str(num))
    # return (lambda x: x == sum(int(i) ** d for i in str(x)))(num)


def gen_narcissistic(digit: int) -> int:
    return [x for x in range(10 ** (digit - 1), 10**digit) if is_narcissistic(x)]


if __name__ == "__main__":
    # 1
    # num = random.randint(100, 999)
    # print(num)
    # print(is_narcissistic(num))

    # 2
    num = gen_narcissistic(3)
    print(num)
