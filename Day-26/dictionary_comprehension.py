"""Dictionary Comprehension"""
import random

names = ["Herin", "Yash", "Vansh", "Aditya", "Heneel", "Teesh"]
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

passed_student = {student:score for (student, score) in student_score.items() if score >=60}
print(passed_student)
