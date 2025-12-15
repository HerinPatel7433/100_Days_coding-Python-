import random
import Hangman_words
import Hangman_art

choose_word = random.choice(Hangman_words.word_list)
lives = 6

print(Hangman_art.logo)
print("Welcome to Hangman!")

placeholder = ""
word_length = len(choose_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letters = []

game_over = False

while not game_over:
    print(f"*************************{lives}/6 Lives Left *************************")
    guess = input("Guess a letter:").lower()
    print(guess)

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display  = ""

    for letter in choose_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if guess not in choose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("*************************You Lose. Choose Word was " + choose_word + "*************************")          

    if "_" not in display:
        game_over = True
        print("*************************You Win. Choose Word was " + choose_word + "*************************")

    print(Hangman_art.stages[lives])