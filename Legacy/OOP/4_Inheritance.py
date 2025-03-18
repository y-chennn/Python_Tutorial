# Inheritance


class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.__age = age
        self.__id = id

    def speak(self, says):
        return self.name + "says" + says


class Athlete(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)

    def workout(self):
        return f"{self.name} goes to the gym twice a week"


# multiple inheritance
class Animal:
    def eat(self):
        print("eating ...")


class Flyable:
    def fly(self):
        print("flying ...")


class Swimmable:
    def swim(self):
        print("swimming ...")


class Duck(Animal, Flyable, Swimmable):
    pass
