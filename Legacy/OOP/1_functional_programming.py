# Functional programming

students = []


def add_student(name, age, grades):
    student = {"name": name, "age": age, "grades": grades}
    students.append(student)


def get_grade_average(student):
    return sum(student["grades"]) / len(student["grades"])


add_student("123", 20, [90, 100, 90, 80])
add_student("456", 22, [70, 60, 60, 70])

for s in students:
    avg = get_grade_average(s)
    print(avg)
