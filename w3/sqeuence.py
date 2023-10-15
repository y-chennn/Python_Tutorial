# List
x = [1, 2, 4, 6, 7, 8]
y = ['cat', 'hog', 'bird']
z = ['hello', 'world', 1, 2, 3, 'go']

m = [['hello world'], 'hola mundo']

# print(x, type(x))
# x[0] = 100
# print(x)
# print(x[-1], x[-3])
# print(x[0], x[1])
# print(y[0])
# print(x + y)
# print(z[1], z[4])

# print(m)
# print(m[0][1])
# m.append('Hallo Welt')
# print(m)

# Tuple
t = (1, 2, 3, 5, 6)
# print(t, type(t))
xt = tuple(x)
# print(xt, type(xt))
t2 = (t, xt)
# print(t2)

# import sys
# list_a = [1, 2, 3, 4, 5]
# tuple_a = (1, 2, 3, 4, 5)

# list_a[0] = 100
# print(list_a)

# tuple_a[0] = 100
# print(tuple_a)

# print(sys.getsizeof(list_a), sys.getsizeof((tuple_a)))


# Set
s = {1, 2, 3, 4, 5, 6}
ss= {1, 2, 1, 1, 3, 5, 6}
# print(s)
# print(ss)
# print(ss.intersection(s))
# print(ss.union(s))
# s.add(99)
# print(s)


nl = []
# nl = list()
nt = ()
# nt = tuple()
ns = {}
# ns = set()
# print(type(nl), type(nt), type(ns))