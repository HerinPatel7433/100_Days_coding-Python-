height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print("Your BMI is: " + str(round(bmi,2)))

# using f-string

print(f"Your BMI is: {round(bmi,2)}")
