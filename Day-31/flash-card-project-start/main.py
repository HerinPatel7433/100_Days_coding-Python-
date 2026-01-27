"""Flash Card Project with Pandas and Tkinter (German to English)"""

import pandas as pd
import tkinter as tk
import random 

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
flip_timer = None

try:
    data = pd.read_csv("Day-31\\flash-card-project-start\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Day-31\\flash-card-project-start\\data\\German_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    
    if flip_timer:
        window.after_cancel(flip_timer)
    
    if len(to_learn) > 0:
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="German", fill="black")
        canvas.itemconfig(card_word, text=current_card["German"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        flip_timer = window.after(3000, func=flip_card)

    else:
        canvas.itemconfig(card_title, text="Completed!", fill="black")
        canvas.itemconfig(card_word, text="All words learned!", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)



def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
        
        data_to_save = pd.DataFrame(to_learn)
        data_to_save.to_csv("Day-31\\flash-card-project-start\\data\\words_to_learn.csv", index=False)
    
    next_card()


# -------------------------------------------- UI Setup -------------------------------------------

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\card_front.png")
card_back_img = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\wrong.png")
unknown_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card, border=0)
unknown_button.grid(row=1, column=0)


check_image = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\right.png")
known_button = tk.Button(image=check_image, highlightthickness=0, command=is_known, border=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()