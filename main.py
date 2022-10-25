import time
from turtle import Screen
from player import Player
import car_manager
from scoreboard import Scoreboard, CAR_SPEED

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
vehicles = car_manager.CarManager()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(CAR_SPEED)
    screen.update()
    vehicles.moves()

    if player.ycor() >= 280:
        time.sleep(1)
        CAR_SPEED *= 0.9
        player.new_level_start()
        scoreboard.increase_level()
        time.sleep(1)

    for block in vehicles.cars:
        if block.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()