from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.begin_fill()
        self.goto(0, -50)
        self.begin_fill()
        self.circle(50)
        self.end_fill()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.goto(0, 300)
        self.goto(0, -300)
        self.penup()
        self.goto(-400, 300)
        self.pendown()
        self.goto(400, 300)
        self.goto(400, -300)
        self.goto(-400, -300)
        self.goto(-400, 300)
