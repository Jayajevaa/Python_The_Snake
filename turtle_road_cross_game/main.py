# TODO 1 : make the turtle move with key press
from turtle import Screen
from player import Player
import time
from cars import CarManager
from score import Score


screen = Screen()
screen.setup(width=1200, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")

score.game_is_on = True
while score.game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    # detect collision with cars
    for cars in car.all_cars:
        if cars.distance(player) < 25:

            score.game_over()

    if player.is_at_finish_line():
        player.restart()
        score.increase_score()
        car.level_up()

screen.exitonclick()
