from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
# from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Crossing Turtle Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect succcessful crossing
    if player.is_at_finish_line():
        player.move_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()