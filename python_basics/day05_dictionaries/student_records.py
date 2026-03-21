students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}


def add_student(name, marks):
    students[name] = marks


def get_topper():
    return max(students, key=students.get)


add_student("David", 95)

print("All Students:", students)
print("Topper:", get_topper())