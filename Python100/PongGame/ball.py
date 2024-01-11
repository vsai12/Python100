from turtle import Turtle
MOVE_AMT = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.x_dir = 1
        self.y_dir = 1
        self.move_spd = 0.1
        self.penup()

    def refresh(self):
        new_x = self.xcor() + self.x_dir * MOVE_AMT
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
        new_y = self.ycor() + self.y_dir * MOVE_AMT
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_dir *= -1
        self.move_spd *= 0.9

    def bounce_x(self):
        self.x_dir *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_spd = 0.1
