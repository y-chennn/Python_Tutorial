from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name) -> None:
        self.__name = name

    @abstractmethod
    def roar(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name)
        self.__breed = breed

    # def roar(self):
    #     print("Woof!")


dog = Dog("dookki", "Collie")
