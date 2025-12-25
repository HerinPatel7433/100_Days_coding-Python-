from turtle import Turtle, Screen
from paddle import Paddle

Screen = Screen()
Screen.bgcolor("black")
Screen.setup(width=800, height=600)
Screen.title("Pong")
Screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




Screen.listen()
Screen.onkey(r_paddle.go_up, "Up")
Screen.onkey(r_paddle.go_down, "Down")
Screen.onkey(l_paddle.go_up, "w")
Screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    Screen.update()


Screen.exitonclick()