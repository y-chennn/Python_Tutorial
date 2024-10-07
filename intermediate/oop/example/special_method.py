# __str__
class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return f"Dog name is {self.name}"


dog = Dog("Dokki")
print(dog)
