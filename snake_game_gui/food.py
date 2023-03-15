from turtle import Turtle
from random import *


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-260, 260)
        random_y = randint(-260, 260)
        self.goto(random_x, random_y)

