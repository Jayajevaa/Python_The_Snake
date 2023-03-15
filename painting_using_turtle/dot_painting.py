import turtle as t
import random

tim = t.Turtle()
tim.hideturtle()

a = -350
b = 300

rad = 3

for i in range(70):
    a = -350
    for j in range(70):
        tim.speed("fastest")
        tim.penup()
        tim.goto(a, b)
        tim.pendown()

        a += 10
        t.colormode(255)
        tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        tim.begin_fill()
        tim.circle(rad)
        tim.end_fill()

        tim.penup()
        tim.forward(10)
        tim.pendown()

    b -= 10

screen = t.Screen()
screen.exitonclick()

