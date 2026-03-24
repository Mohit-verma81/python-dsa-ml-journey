class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        avg = self.get_average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        else:
            return "C"


# Usage
s1 = Student("Alice", [85, 90, 88])
print("Average:", s1.get_average())
print("Grade:", s1.get_grade())