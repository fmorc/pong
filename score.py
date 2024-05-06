import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT=("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.sety(260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score_left} - {self.score_right}", align=ALIGNMENT, font=FONT)


    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()



