import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

WIDTH = 800
HEIGHT = 600
INITIAL_SPEED = 0.1
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle_left = Paddle(-370)
paddle_right = Paddle(370)
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle_left.up, "q")
screen.onkeypress(paddle_left.down, "a")
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")


def right_paddle_collision():
    return ball.distance(paddle_right) < 50 and ball.xcor() > 340


def left_paddle_collision():
    return ball.distance(paddle_left) < 50 and ball.xcor() < -340


def paddle_collision():
    return right_paddle_collision() or left_paddle_collision()


speed = INITIAL_SPEED
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_reverse()
        speed *= 0.9
    if paddle_collision():
        ball.horizontal_reverse()
        speed *= 0.9
    if ball.xcor() > 360:
        score.increase_score_left()
        speed = INITIAL_SPEED
        ball.restart()
    if ball.xcor() < -360:
        score.increase_score_right()
        speed = INITIAL_SPEED
        ball.restart()


screen.exitonclick()
