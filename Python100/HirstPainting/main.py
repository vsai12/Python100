# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract("hirst.jpeg", 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107)]
tim = Turtle()
turtle.colormode(255)
tim.begin_fill()
tim.speed("fastest")
tim.penup()
tim.goto(-200, -200)
tim.pendown()

for y in range(10):
    for _ in range(10):
        tim.color()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.goto(-200, -200 + 50 * (y + 1))
    tim.pendown()
tim.hideturtle()

display = Screen()
display.exitonclick()

