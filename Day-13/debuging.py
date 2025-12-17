"""Debugging example module."""
"""Describe the problem 
    1. what is the loop doing?
    2. when is the fuction meant to print Reached 20?
    3. what are your assumptions about the value of i?"""

def my_fuction():
    # for i in range(1 , 20): # Loop stops at 19, should be 21 to include 20
    for i in range(1 , 21):
        if i == 20:
            print("Reached 20!") 

my_fuction()

# Reproduce the bug

from random import randint
dice_images = ["1" , "2" , "3" , "4" , "5" , "6"]
# dice_num = randint(1, 6) will produce an indexing error
dice_num = randint(1, 5)
print(dice_images[dice_num])

# Play Computer

year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994: this will produce error when 1994 is enter as it is not included in nither
if year > 1980 and year <=1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix the errors

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a invalid number. please try again with a numerical value like 15.")
    age = int(input("How old are you?"))

if age > 18:
    # print("You can drive at age {age}") this will not produce error but it will also not give input you wnated due statment not being f-string
    print(f"You can drive at age {age}")