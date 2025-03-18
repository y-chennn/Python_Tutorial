from animal import Animal
from flyable import Flyable
from swimmable import Swimmable


class Duck(Animal, Flyable, Swimmable):
    pass
