height = int(input("Enter your height in cm: "))
tickets = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Child tickets are $5")
        tickets = 5
    elif age <= 18:
        print("Youth tickets are $7")
        tickets = 7
    else:
        print("Adult tickets are $12")
        tickets = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        print("Photo taken! An extra $3 will be added to your bill.")
        tickets += 3
        print(f"Your total bill is ${tickets}")
    else:
        print("No photo will be taken.")
        print(f"Your total bill is ${tickets}")
else:
    print("sorry you have to grow taller before you can ride")
