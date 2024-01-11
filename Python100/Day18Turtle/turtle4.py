from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed(5)

display = Screen()
display.colormode(255)

for _ in range(100):
    tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    choice = random.randint(0,4)
    if choice == 0:
        tim.forward(10)
    elif choice == 1:
        tim.left(90)
        tim.forward(10)
    elif choice == 2:
        tim.right(90)
        tim.forward(10)
    else:
        tim.right(180)
        tim.forward(10)

display.exitonclick()