import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.pu()
        car.seth(180)
        car.shape('square')
        car.turtlesize(1, 3)
        car.setpos(320, random.randint(-280, 280))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.fd(self.speed)
            if car.xcor() < -350:
                self.cars.remove(car)
            else:
                pass
    
    def level_up(self):
        self.speed += MOVE_INCREMENT

    def collision_check(self, player):
        for car in self.cars:
            if car.distance(player) < 5:
                return False
            else:
                pass
        return True
    

        

