classroom = [
    {'name':'Willy', 'gender':'male', 'grade':'80'},
    {'name':'Paul', 'gender':'male', 'grade':'85'},
    {'name':'Dorcas', 'gender':'female', 'grade':'85'},
    {'name':'Faith', 'gender':'female', 'grade':'80'},
    {'name':'Maingi', 'gender':'male', 'grade':'70'}
]

# listing all students
# updating students grade

def list_students():
    for student in classroom:
        print(f'{student.get("name")}')

def update_student_grade(studentname, newgrade):
    student = [stud for stud in classroom if stud.get('name')==studentname]
    if student.count == 0:
        print('Student does not exist')
    else:
        student[0]['grade'] = newgrade
        print('Student updated')

def view_updated_grade(studentname):
    student = [stud for stud in classroom if stud.get('name')==studentname]
    print(
    f'''
Name: {student[0].name}
Gender: {student[0].gender}
Grade: {student[0].grade}
    ''')

def main():
    selectOption = input('>> ')

    if selectOption == '0':
        exit()
    elif selectOption == '1':
        list_students()
    elif selectOption == '2':
        studentname = input('Student name: ')
        newgrade = input('New grade: ')

        update_student_grade(studentname, newgrade)

    elif selectOption == '3':
        studentname = input('Student name: ')
        view_updated_grade(studentname)

    else:
        print('Invalid option')

    main()

if __name__ == '__main__':
    options = '''
Program options:
0 - Exit program
1 - List all students
2 - Update student grade
3 - View Student
    '''
    print(options)

    main()
    
