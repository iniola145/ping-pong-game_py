from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.color("white")
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5, outline=1)
        self.penup()
        self.goto(location)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
