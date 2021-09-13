##!/usr/bin/python
from turtle import Screen
from turtle import Turtle
from random import randint
import time

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
        heading = randint(0, 360)
        self.seth(heading)
    
    def go(self):
        self.forward(1)
        if abs(self.ycor()) >= 275:
            self.bounce()
    
    def reset(self):
        self.setpos(0,0)
        heading = randint(0, 360)
        self.seth(heading)

    def bounce(self):
        if self.heading() < 90 and self.heading() > 0:
            self.seth(self.heading() + 270)
            self.forward(20)
        elif self.heading() > 90 and self.heading() < 180:
            self.seth(self.heading() + 90)
            self.forward(20)
        elif self.heading() > 180 and self.heading() < 270:
            self.seth(self.heading() - 90)
            self.forward(20)
        elif self.heading() > 270 and self.heading() < 360:
            self.seth(self.heading() - 270)
            self.forward(20)
        else:
            pass

    def paddle_bounce(self):
        if self.heading() < 90 and self.heading() > 0:
            self.seth(self.heading() + 90)
            self.forward(20)
        elif self.heading() > 90 and self.heading() < 180:
            self.seth(self.heading() + 90)
            self.forward(20)
        elif self.heading() > 180 and self.heading() < 270:
            self.seth(self.heading() + 90)
            self.forward(20)
        elif self.heading() > 270 and self.heading() < 360:
            self.seth(self.heading() - 90)
            self.forward(20)
        else:
            pass

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.left = 0
        self.right = 0
        self.setpos(-50, 280)
        self.write(str(self.right) + ' - ' + str(self.left))
        self.side = None
    def score(self, side):
        self.side = side
        if self.side.lower() == 'left':
            self.left = self.left + 1
        elif self.side.lower() == 'right':
            self.right = self.right + 1
        else:
            pass
        self.clear()
        self.write(str(self.right) + ' - ' + str(self.left))

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
    scoreboard = ScoreBoard()
    while game_on:
        ball.go()
        screen.update()
        if abs(ball.xcor()) >= 375 and (ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50):
            ball.paddle_bounce()
        if ball.xcor() > 400:
            scoreboard.score('right')
            ball.reset()
        elif ball.xcor() < -400:
            scoreboard.score('left')
            ball.reset()
        time.sleep(0.005)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
    
    