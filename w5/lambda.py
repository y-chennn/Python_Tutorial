# lambda arg_list:expression

# lambda x, y: x + y


def func(x, y):
    return x + y


# print(func(1, 2))


# add = lambda x, y, z: x + y + z
# print(add(1, 2, 3))

# print((lambda x, y: x + y)(1, 2))

num = [1, 25, 69, 38, 197]
res = filter(lambda x: x > 10, num)
print(res)
# print(list(res))
