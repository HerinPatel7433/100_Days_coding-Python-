"""Flash Card Project with Pandas and Tkinter (German to English)"""

import pandas as pd
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
# -------------------------------------------- UI Setup -------------------------------------------

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\card_front.png")
canvas.create_image(400, 263,image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\wrong.png")
unknown_button = tk.Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)


check_image = tk.PhotoImage(file="Day-31\\flash-card-project-start\\images\\right.png")
known_button = tk.Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()