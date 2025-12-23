import turtle

grey = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    grey.forward(10)

def move_backward():
    grey.backward(10)

def move_right():
    grey.right(5)

def move_left():
    grey.left(5)

def clear_drawing():
    grey.setposition(0 , 0)
    grey.setheading(0)
    grey.clear()

def circle():
    for _ in range(int(360/5)):
        move_forwards()
        move_left()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="o", fun=circle)

screen.exitonclick()
