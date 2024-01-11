import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.up()
tim.setx(-250)
tim.down()

for _ in range(50):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()

display = Screen()
display.exitonclick()