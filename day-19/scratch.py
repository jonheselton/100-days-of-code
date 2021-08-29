##!/usr/bin/python
from turtle import Turtle, Screen
from random import randint


def etchnsketch():
    def fd():
        t.fd(5)

    def lf():
        t.right(-15)

    def rt():
        t.right(15)

    def bk():
        t.back(5)

    t = Turtle()
    screen = Screen()
    screen.onkey(fd, 'w')
    screen.onkey(lf, 'a')
    screen.onkey(bk(), 's')
    screen.onkey(rt, 'd')
    screen.listen()

    screen.exitonclick()


class Race:

    def __init__(self):
        racers = []
        self.blue = Turtle()
        self.blue.color('blue')
        self.blue.pu()
        self.blue.setposition(0, 0)
        self.red = Turtle()
        self.red.pu()
        self.red.color('red')
        self.red.setpos(0, 40)
        self.yellow = Turtle()
        self.yellow.pu()
        self.yellow.color('yellow')
        self.yellow.setposition(0, 100)
        self.orange = Turtle()
        self.orange.color('orange')
        self.orange.pu()
        self.orange.setposition(0, 150)
        self.green = Turtle()
        self.green.pu()
        self.green.color('green')
        self.green.setposition(0, 200)
        self.racers = [self.blue, self.red, self.orange, self.green, self.yellow]
        self.winner = None
        
    def go(self):
        for racer in self.racers:
            racer.forward(randint(0, 10))
            if self.race_over(racer):
                return "We have a winner"
            else:
                return self.go()

    def race_over(self, competitor):
        if competitor.pos()[0] > 255:
            return competitor


def main():
    screen = Screen()
    race = Race()
    won = race.go()
    print(won)

    screen.exitonclick()
    return


if __name__ == "__main__":
    main()
