from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.game_on = True

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Ariel", 50, "bold"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Ariel", 50, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        if self.r_score == 11:
            self.goto(0, 100)
            self.write("Right player won", align="center", font=("Ariel", 50, "bold"))
            self.game_on = False
        if self.l_score == 11:
            self.goto(0, 100)
            self.write("Left player won", align="center", font=("Ariel", 50, "bold"))
            self.game_on = False
