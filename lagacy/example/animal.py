class Animal:
    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        return print(f"{self.__name}")

    def roar(self):
        print("roar")


class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name)
        self.__breed = breed

    # def get_name(self):
    #     return print(f"{self.__name}")

    def roar(self):
        print("Woof!")


class Corgi(Dog):
    def __init__(self, name, breed, age) -> None:
        super().__init__(name, breed)
        self.__age = age

    def get_age(self):
        return print(f"{self.__age}")


dog = Dog("Dokki", "Collie")
dog.get_name()

corgi = Corgi("ball", "Corgi", "3")
corgi.get_age()
corgi.get_name()
