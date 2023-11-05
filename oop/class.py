s = "hello"
# print(type(s))


class dog:
    def __init__(self, name) -> None:
        self.name = name

    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1

    def get_name(self):
        return self.name


d = dog("123")
# print(type(d))
# d.bark()
# print(d.add_one(5))
print(d.get_name())
