import turtle
import random
turtle.colormode(255)
grey = turtle.Turtle()
grey.shape("arrow")
grey.speed("fastest")
grey.hideturtle()

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)

def draw_spirogarph(gap, lenght):
    no_of_circles = int(360/gap)

    for _ in range(no_of_circles):
        grey.circle(lenght)
        current_heading = grey.heading()
        grey.setheading(current_heading + gap)
        grey.color(get_random_color())

draw_spirogarph(5, 100)
screen = turtle.Screen()
screen.exitonclick()