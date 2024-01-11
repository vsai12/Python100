from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.x_pos = x_pos
        self.penup()
        self.goto(self.x_pos, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_pos, new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_pos, new_y)
