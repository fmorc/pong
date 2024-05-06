from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("aqua")
        self.y_change = 10
        self.x_change = 10

    def move_right_up(self):
        new_xcor = self.xcor() + 10
        new_ycor = self.ycor() + 10
        self.setposition(new_xcor, new_ycor)

    def move_right_down(self):
        new_xcor = self.xcor() + 10
        new_ycor = self.ycor() - 10
        self.setposition(new_xcor, new_ycor)

    def move_left_down(self):
        new_xcor = self.xcor() - 10
        new_ycor = self.ycor() - 10
        self.setposition(new_xcor, new_ycor)

    def move_left_up(self):
        new_xcor = self.xcor() - 10
        new_ycor = self.ycor() + 10
        self.setposition(new_xcor, new_ycor)

    def move(self):
        new_xcor = self.xcor() + self.x_change
        new_ycor = self.ycor() + self.y_change
        self.setposition(new_xcor, new_ycor)

    def vertical_reverse(self):
        self.y_change *= -1

    def horizontal_reverse(self):
        self.x_change *= -1

    def restart(self):
        new_xcor = 0
        new_ycor = 0
        self.horizontal_reverse()
        self.setposition(new_xcor, new_ycor)
