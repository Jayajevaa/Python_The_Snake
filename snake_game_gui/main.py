from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

speed_delay = [0.2, 0.15]
screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.bgpic("bg_1.png")

screen.tracer(0)

# TODO 0.1 :make border
border = Turtle()
border.hideturtle()
border.pencolor("white")
border.pensize(2)
border.penup()
border.goto(x=290, y=-290)
border.pendown()
border.goto(x=290, y=290)
border.goto(x=-290, y=290)
border.goto(x=-290, y=-290)
border.goto(x=290, y=-290)
# TODO 1 : make snake body with 3 squares
snake = Snake()
food = Food()
score = Score()

# TODO 3 : control the snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")



# TODO 2 : move the snake

while score.game_on:
    screen.update()
    if score.score >= 10:
        num = 1
    else:
        num = 0
    time.sleep(speed_delay[num])

    snake.move()
    #DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()
    #DETECT COLLISION WITH WALL

    #if snake.head.xcor() > 295 or snake.head.xcor() < -295:
    #    score.game_over()
    #if snake.head.ycor() > 295 or snake.head.ycor() < -295:
    #    score.game_over()
    if snake.head.xcor() > 290:
        snake.head.goto(-280, snake.head.ycor())
    if snake.head.xcor() < -290:
        snake.head.goto(280, snake.head.ycor())
    if snake.head.ycor() > 290:
        snake.head.goto(snake.head.xcor(), -280)
    if snake.head.ycor() < -290:
        snake.head.goto(snake.head.xcor(), 280)



    #DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            with open('high_score.txt', mode='w') as file:
                file.write(str(score.high_score))




# TODO 4 : detect collision with food
# TODO 5 : create score board
# TODO 6 : detect collision with wall
# TODO 7 :detect collision with tail


screen.exitonclick()

