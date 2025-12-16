"""This is number guessing game project."""
import random
import Number_guessing_game_art

def number_guessing_game():
    print(Number_guessing_game_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
        return
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            return
        
        attempts -= 1
        
        if attempts == 0:
            print(f"You've run out of guesses. The number was {number_to_guess}. Game over.")

number_guessing_game()