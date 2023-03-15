from turtle import *


FONT = ("Arial", 24, "normal")
ALLIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open('high_score.txt', mode='r') as file:
            h_s = file.read()
            self.high_score = int(h_s)
        self.game_on = True
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 290)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"SCORE : {self.score}   HIGH SCORE : {self.high_score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 5
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
    #def game_over(self):
    #    self.game_on = False
    #
    #    self.goto(0, -50)
    #    self.color("black")
    #    self.color("white")
    #    self.write(f"GAME OVER!", align=ALLIGNMENT, font=("Ariel", 50, "normal"))