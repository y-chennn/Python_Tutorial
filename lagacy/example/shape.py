class Shape:
    def __init__(self, color, length, width) -> None:
        self._color = color
        self._length = length
        self._width = width

    # instance method
    def display(self):
        print(f"{self._color}, length: {self._length}, width: {self._width}")

    # static method
    @staticmethod
    def cal_area(length, width):
        return length * width

    # classmethod
    @classmethod
    def create_square(cls, color, length):
        return cls(color, length, length)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


rectangle = Shape("red", 3, 4)
rectangle.display()

l, w = 5, 20
area = rectangle.cal_area(l, w)
print(f"area = {area}")

square = Shape.create_square("yellow", 3)

rectangle.color = "green"
