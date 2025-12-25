from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

        self.dy = 0        # vertical speed

    def move(self):
        new_y = self.ycor() + self.dy
        # optional: keep paddle inside screen
        if -260 < new_y < 260:
            self.goto(self.xcor(), new_y)

    def start_up(self):
        self.dy = 20

    def start_down(self):
        self.dy = -20

    def stop(self):
        self.dy = 0
