from turtle import Turtle
FONT = ("Courier", 80, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=FONT)

    def p1_goal(self):
        self.p1_score += 1
        self.update()

    def p2_goal(self):
        self.p2_score += 1
        self.update()
