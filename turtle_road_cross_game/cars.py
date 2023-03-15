from turtle import Turtle
from random import *

COLORS = ["red", "orange", "pink", "blue", "brown", "aqua", "black"]
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = randint(1, 7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(600, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

