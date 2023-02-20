import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")
cars: list[CarManager] = []
game_is_on = True

counter = 0
while game_is_on:
    time.sleep(0.1)

    if counter % 6 == 0:
        car = CarManager()
        cars.append(car)
    counter += 1
    if player.finishing_line():
        scoreboard.level_up()
        CarManager.speed_inc()
    for car in cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
        car.move()

    screen.update()
screen.exitonclick()
