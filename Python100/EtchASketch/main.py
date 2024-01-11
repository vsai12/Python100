import turtle
from turtle import Turtle, Screen

tim = Turtle()
display = Screen()
display.listen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()


display.onkeypress(move_forward, "w")
display.onkeypress(move_backwards, "s")
display.onkeypress(counter_clockwise, "a")
display.onkeypress(clockwise, "d")
display.onkeypress(clear, "c")

display.exitonclick()