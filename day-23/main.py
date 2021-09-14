import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
player = Player()
score_board = Scoreboard()
screen.onkey(player.move, "Up")
screen.tracer(0)
car_manager = CarManager()
car_manager.new_car()


game_is_on = True
while game_is_on:
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()
    if random.randint(0,20) == 5:
        car_manager.new_car()
    else:
        pass
    game_is_on = car_manager.collision_check(player)
    if player.score():
        score_board.next_level()
        car_manager.level_up()

print(game_is_on)