from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=1000, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win, enter a color :")

color = ["red", "orange", "purple", "blue", "green"]
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []

for _ in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color[_])
    new_turtle.goto(x=-480, y=y_positions[_])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 450:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You won the bet, the {win_color} turtle won the race")
            else:
                print(f"Yu have lost the bet, the {win_color} turtle won the race")
            print(turtle.color)
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()