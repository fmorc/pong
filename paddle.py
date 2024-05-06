from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.x_position = position
        self.create_paddle()

    def create_paddle(self):
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color("white")
        self.setposition(self.x_position, 0)

    def up(self):
        if self.ycor() < 240:
            new_ycor = self.ycor() + 20
            self.setposition(self.x_position, new_ycor)

    def down(self):
        if self.ycor() > -240:
            new_ycor = self.ycor() - 20
            self.setposition(self.x_position, new_ycor)

