s = "hello"
# print(type(s))


class dog:
    pass


dog1 = dog()
dog1.name = "poppy"
dog1.breed = "Chihuahua"
dog1.num = 1


dog2 = dog()
dog2.name = "poppy2"
dog2.breed = "dachshund"
dog2.num = 2

# print(dog1.name)


class dog:
    def __init__(self, name, breed) -> None:
        self.__name = name
        self.__breed = breed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


dog3 = dog("poppy", "Chihuahua")
# print(dog3.name)
# dog3.name = "popo"
# print(dog3.__name)
print(dog3.get_name())
dog3.set_name("popo")
print(dog3.get_name())
