from main import  Student

students = Student.select()
for student in students:
    print(student.stud_name, student.stud_email, student.stud_password)