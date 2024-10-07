import math
from abc import ABC, abstractmethod


class ShapeBase(ABC):
    def __init__(self, color) -> None:
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    @abstractmethod
    def area(self):
        pass


class Circle(ShapeBase):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"The radius of the circle is {self.radius}."


class Rectangle(ShapeBase):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"The dimensions of the rectangle are {self.length} x {self.width}."
