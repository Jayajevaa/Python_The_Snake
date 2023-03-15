from turtle import Turtle
import time

STARTING_POSITION = [(-0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.foods = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates a snake with 3 segments"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        """this makes the n th seg goto the previous position of seg n-1 and thus all segments follow the head"""
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        #self.head.setheading(UP)
        #self.head.forward(5)
        #self.head.setheading(DOWN)
        #self.head.forward(5)



    def move_up(self):
        """this sets the heading of the head to 90 deg"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """this sets the heading of the head to 270 deg"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """this sets the heading of the head to 180 deg"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """this sets the heading of the head to 0 deg"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        time.sleep(3)
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())