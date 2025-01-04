
from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
class CarManager:
    def __init__(self):
        self.cars = []
    def create_car(self):
        color = rd.choice(COLORS)
        car = Turtle()
        car.color(color)
        car.shape("square")
        car.setheading(180)
        car.turtlesize(1, 2)
        car.penup()
        self.cars.append(car)
        new_x = rd.randrange(300, 1500, 60)
        # new_x = 300
        new_y = rd.randrange(-250, 250, 50)
        car.goto(new_x, new_y)
    def move(self):
        for cars in self.cars:
            cars.forward(STARTING_MOVE_DISTANCE)
    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    def remove_car(self):
        for car in self.cars:
            if car.xcor() < - 350:
                self.cars.remove(car)
