from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

X_POS = 350


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1 = Paddle(-X_POS)
p2 = Paddle(X_POS)
b = Ball()
score = ScoreBoard()
game_is_on = True

screen.listen()
screen.onkey(p1.up, "w")
screen.onkey(p1.down, "s")
screen.onkey(p2.up, "Up")
screen.onkey(p2.down, "Down")

while game_is_on:
    time.sleep(b.move_spd)
    screen.update()

    b.refresh()
    if b.distance(p2) < 50 and b.xcor() > 320 or b.distance(p1) < 50 and b.xcor() < -320:
        b.bounce_x()

    if b.xcor() > 380:
        b.reset_pos()
        score.p1_goal()

    if b.xcor() < -380:
        b.reset_pos()
        score.p2_goal()

screen.exitonclick()