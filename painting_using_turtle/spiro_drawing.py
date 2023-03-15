import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


def random_color():
    """chooses random values btw 0 to 255 for r g and b and returns a tupple (r, g, b)"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


direction = [0, 90, 180, 270]
tim.pensize(1)
tim.speed("fastest")


def draw_spiro_graph(gap):
    for i in range(int(360/gap)):
        tim.color(random_color())
        for num in range(100, 0, -20):
            tim.circle(num)
        current_heading = tim.heading()
        tim.setheading(current_heading + gap)


draw_spiro_graph(10)


screen = t.Screen()
screen.exitonclick()

