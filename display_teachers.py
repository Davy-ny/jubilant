from main import Teacher

Teacher =Teacher.select()
for teacher in teachers:
    print(teacher.teach_name, teacher.teach_email, teacher.teach_password)