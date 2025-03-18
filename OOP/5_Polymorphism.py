# Polymorphism


# method overriding
class Animal:
    def sound(self):
        return "sound"


class Cat(Animal):
    def sound(self):
        return "meow"


class Dog(Animal):
    def sound(self):
        return "bow-wow"


# method overloading
class Calulator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
