# Encapsulation


class Student:
    def __init__(self, name, age, major):
        self.__name = name
        self.__age = age
        self.__major = major

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_info(self):
        return {"name": self.__name, "age": self.__age, "major": self.__major}


students = [Student("123", 20, "ee"), Student("456", 20, "ee")]

for s in students:
    print(s.get_info())
