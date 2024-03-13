######## One to Many Relationship

class Mentor:
    def __init__(self, name):
        self.name = name
        self.students = []

    def assign_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name

# create mentor
mentor1 = Mentor('Jane')

# students
stud1 = Student('Nicole')
stud2 = Student('John')
stud3 = Student('Sang')

# assign students
mentor1.assign_student(stud1)
mentor1.assign_student(stud2)
mentor1.assign_student(stud3)

for stud in mentor1.students:
    print(stud.name)