##!/usr/bin/python
from turtle import Screen
from turtle import Turtle
from random import randint

class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.pu()
        if self.side.lower() == 'right':
            self.setpos(390, 0)
        elif self.side.lower() == 'left':
            self.setpos(-390, 0)
        else:
            pass

    def mup(self):
        self.setpos(self.xcor(), self.ycor() + 20)

    def mdw(self):
        self.setpos(self.xcor(), self.ycor() - 20)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.setpos(0,0)
    
    def start(self):
        if randint(0,1) == 1:
            heading = randint(36, 125)
        else:
            heading = randint(215, 305)
        self.seth(heading)
    
    def go(self):
        self.forward(20)

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.tracer(0)
    r_paddle = Paddle('right')
    l_paddle = Paddle('left')
    ball = Ball()

    screen.listen()
    screen.onkey(r_paddle.mup, 'Up')
    screen.onkey(r_paddle.mdw, 'Down')
    screen.onkey(l_paddle.mup, 'w')
    screen.onkey(l_paddle.mdw, 'a')
    game_on = True
    
    while game_on:
        ball.go()
        screen.update()
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
    
    