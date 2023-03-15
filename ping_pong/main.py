from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
from board import Board


# TODO 1 : create screen setting
screen = Screen()
screen.bgcolor("black")
screen.setup(height=650, width=850)
screen.title("PING-PONG")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Score()
board = Board()

screen.listen()


screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_up, "w")

screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_down, "s")


while score.game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # detect paddle misses ball
    if ball.xcor() > 390:
        score.l_point()
        ball.reset_ball()

    if ball.xcor() < -390:
        score.r_point()
        ball.reset_ball()
    score.game_over()


screen.exitonclick()
