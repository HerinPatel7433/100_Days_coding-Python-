import turtle as t
import time
from sanke import Sanke

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

sanke = Sanke()

screen.listen()
screen.onkey(sanke.up, "Up")
screen.onkey(sanke.down, "Down")
screen.onkey(sanke.right, "Right")
screen.onkey(sanke.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    sanke.move()

screen.exitonclick()