class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grade(self):
        return sum(self.grades) / len(self.grades)


students = [Student("123", 20, [90, 100, 90, 80]), Student("456", 20, [70, 60, 60, 70])]

for s in students:
    avg = s.get_avg_grade()
    print(avg)
