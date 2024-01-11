import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
car_manager.generate()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
counter = 0
wait_time = random.randint(1, 6)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter == wait_time:
        car_manager.generate()
        counter = 0
        wait_time = random.randint(1, 6)
    else:
        counter += 1
    car_manager.move_cars()

    for car in car_manager.cars[car_manager.off_screen:]:
        if player.distance(car) < 19:
            game_is_on = False
            scoreboard.game_over()
            break

    if player.ycor() > player.end:
        player.level_up()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()
