import random
Choice = ["Rocks" , "Paper" ,"Scissors"] 
Choice[0] = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Choice[1] = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Choice[2] = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:")
print(Choice[user_choice])

print("Computer chose:")
computer_choice = random.randint(0,2)
print(Choice[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")

