#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)
empty = []

j_student_1 = student_1.to_json([])
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['age'])
j_student_4 = student_2.to_json(attrs="invalid")
j_student_5 = student_2.to_json(attrs=[])
j_student_6 = student_2.to_json(attrs=["invalid"])
j_student_7 = student_2.to_json(attrs=None)
print(j_student_1)
print(j_student_2)
print(j_student_3)
print(j_student_4)
print(j_student_5)
print(j_student_6)
print(j_student_7)
