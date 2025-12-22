import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
turtle.colormode(255)

grey = turtle.Turtle()
grey.speed("fastest")
grey.penup()
grey.hideturtle()

def get_random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

grey.setpos(-200, -200)

for row in range(10):
    for col in range(10):
        grey.dot(20, get_random_color())
        grey.forward(40)
    grey.backward(400)
    grey.left(90)
    grey.forward(40)
    grey.right(90)

screen.exitonclick()
