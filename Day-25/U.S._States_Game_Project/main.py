import pandas as pd
import turtle as tur
import time
import os
import random

screen = tur.Screen()
screen.title("U.S. States Game — Find the State")
image = "Day-25\\U.S._States_Game_Project\\blank_states_img.gif"
screen.addshape(image)
tur.shape(image)

data = pd.read_csv("Day-25\\U.S._States_Game_Project\\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

writer = tur.Turtle()
writer.hideturtle()
writer.penup()

target = tur.Turtle()
target.hideturtle()
target.penup()
target.goto(0, 260)

start_time = time.time()

HS_FILE = "high_score.txt"
best_time = None
if os.path.exists(HS_FILE):
    with open(HS_FILE, "r") as f:
        try:
            best_time = float(f.read().strip())
        except:
            best_time = None

current_target = None


def show_state(name, x, y, color="green"):
    writer.goto(int(x), int(y))
    writer.color(color)
    writer.write(name, align="center", font=("Arial", 10, "bold"))


def pick_next_state():

    global current_target

    remaining = [s for s in all_states if s not in guessed_states]

    if not remaining:
        end_game()
        return

    current_target = random.choice(remaining)

    target.clear()
    target.write(
        f"Find: {current_target}",
        align="center",
        font=("Arial", 16, "bold")
    )

    screen.title(f"{len(guessed_states)}/50 Correct — Find {current_target}")


def check_click(x, y):
    global guessed_states, current_target
    
    row = data[data.state == current_target].iloc[0]

    if abs(x - row.x) < 15 and abs(y - row.y) < 15:
        guessed_states.append(current_target)
        show_state(current_target, row.x, row.y, "green")
        pick_next_state()  

def end_game():
    screen.onscreenclick(None)
    target.clear()

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    missed = [s for s in all_states if s not in guessed_states]
    for state in missed:
        row = data[data.state == state].iloc[0]
        show_state(state, row.x, row.y, "red")

    global best_time
    is_record = False
    if best_time is None or total_time < best_time:
        best_time = total_time
        with open(HS_FILE, "w") as f:
            f.write(str(best_time))
        is_record = True

    msg = (
        f"You finished in {total_time} seconds!\n\n"
        f"Best time: {best_time} seconds"
    )
    if is_record:
        msg += "\n🏆 New High Score!"

    tur.textinput("Game Over", msg)
    screen.bye()


screen.onscreenclick(check_click)

pick_next_state()
screen.mainloop()
