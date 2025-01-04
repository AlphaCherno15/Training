import time
from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.onkey(fun=lambda: player.up(), key="Up")
car_manager = CarManager()
game_is_on = True
print(car_manager.cars)
while game_is_on:
    # car_manager.create_car()
    car_manager.move()
    car_manager.remove_car()
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        car_manager.level_up()
        scoreboard.level()
        player.go_home()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()