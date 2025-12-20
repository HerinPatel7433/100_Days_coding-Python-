student_scores = [150, 142, 134 , 128, 163, 178, 192, 145, 87, 94, 100, 99, 89]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")