class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0
    

s = Student("Vicky",14, {"Maths":85, "Science":80, "English":87})
n = s.calculate_average()

print("The Average Number is =", n)
