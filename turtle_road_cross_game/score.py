from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.penup()
        self.goto(-400,260)
        self.hideturtle()
        self.score = 1
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL : {self.score}", align="center", font= ("Ariel", 20, "bold") )

    def game_over(self):
        self.goto(0, 0)
        self.game_is_on = False
        self.write("GAME OVER", align="center", font=("Ariel", 50, "bold"))

