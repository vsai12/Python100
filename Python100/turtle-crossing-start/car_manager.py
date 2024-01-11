from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_spd = STARTING_MOVE_DISTANCE
        self.cars = []
        self.off_screen = 0

    def generate(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        color = random.choice(COLORS)
        new_car.color(color)
        y_pos = random.randint(-250, 250)
        new_car.goto(300, y_pos)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars[self.off_screen:]:
            if car.xcor() < -320:
                self.off_screen += 1
            car.forward(self.move_spd)

    def level_up(self):
        self.move_spd += MOVE_INCREMENT
        for car in self.cars[self.off_screen:]:
            car.goto(500, 500)
        self.cars = []
        self.off_screen = 0
