from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")

#triangle
tim.pencolor("red")
for _ in range(3):
    tim.forward(100)
    tim.right(120)


#square
tim.pencolor("pink")
for _ in range(4):
    tim.forward(100)
    tim.right(90)

#pentagon
tim.pencolor("orange")
for _ in range(5):
    tim.forward(100)
    tim.right(72)

#hexagon
tim.pencolor("yellow")
for _ in range(6):
    tim.forward(100)
    tim.right(60)

#heptagon
tim.pencolor("green")
for _ in range(7):
    tim.forward(100)
    tim.right(51.5)

#octagon
tim.pencolor("light blue")
for _ in range(8):
    tim.forward(100)
    tim.right(45)

#nonagon
tim.pencolor("blue")
for _ in range(9):
    tim.forward(100)
    tim.right(40)

#decagon
tim.pencolor("purple")
for _ in range(10):
    tim.forward(100)
    tim.right(36)

display = Screen()
display.exitonclick()