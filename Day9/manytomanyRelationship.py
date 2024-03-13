####### many to many

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
    
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.enroll(self)

# create students
stud1 = Student('Nicole')
stud2 = Student('John')

# create courses
course1 = Course('Python')
course2 = Course('Java')

course1.add_student(stud1)
course2.add_student(stud1)

course1.add_student(stud2)
course2.add_student(stud2)

for course in stud1.courses:
    print(course.name)