##!/usr/bin/python
from turtle import Screen, Turtle
import random
import time

class Snake:
    
    def __init__(self):
        self.length = 3
        self.segments = []

    def snake(self):
        x = 0
        y = 0
        for i in range(0, self.length):
            segment = Turtle(shape='square')
            segment.color("white")
            segment.pu()
            segment.setpos(x, y)
            x = x + 30
            self.segments.append(segment)
        self.head = self.segments[0]

    def place_fruit(self):
        self.fruit = Turtle('square')
        self.fruit.color('red')
        self.fruit.pu()
        self.fruit.setpos(random.randint(-280, 280), random.randint(-280, 280))

    def snake_eats_fruit(self):
        if self.head.distance(self.fruit) <= 15:
            self.length = self.length + 1
            self.update_segment()
            self.fruit.setpos(random.randint(-280, 280), random.randint(-280, 280))

    def update_segment(self):
        segment = Turtle(shape='square')
        segment.color("white")
        segment.pu()
        segment.setpos(self.segments[-1].position()) 
        self.segments.append(segment)


    def move(self):
        for i in range(len(self.segments)-1, -1, -1):
            if i > 0:
                self.segments[i].goto(self.segments[i-1].position())
            else:
                self.segments[i].fd(20)

    def lf(self):
        if self.head.heading() != 0:
            self.head.seth(180)
    def rt(self):
        if self.head.heading() != 180:
            self.head.seth(0)
    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
    def dn(self):
        if self.head.heading() != 90:
            self.head.seth(270)
    
    def you_lose(self):
        for i in range(1,self.length):
            if self.segments[i].distance(self.head) < 1:
                return False
        if abs(self.head.xcor()) >= 300 or abs(self.head.ycor()) >= 300:
            return False
        else:
            return True

    
def main():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)
    
    game = Snake()
    game.snake()

    screen.onkey(game.up, 'w')
    screen.onkey(game.lf, 'a')
    screen.onkey(game.dn, 's')
    screen.onkey(game.rt, 'd')
    screen.listen()

    game.place_fruit()
    score = Turtle()
    highscore = 0
    game_on = True
    while game_on:
        if highscore < game.length-3:
            highscore = game.length-3
        else:
            pass
        score.clear()
        score.setpos(-39, 280)
        score.color('white')
        score.write("Score: " + str(game.length-3) + "  Highscore: " + str(highscore))
        score.hideturtle()
        game.snake_eats_fruit()
        screen.update()
        time.sleep(0.1)
        game.move()
        game_on = game.you_lose()
        if game_on == False:
            loser = Turtle()
            loser.clear()
            loser.color('white')
            loser.write('You Lose - Play Again? (y/n)')
            screen.update()
            response = input('Play again? ')
            if response == 'y':
                game_on = True
                game = Snake()
                game.snake()
                game.place_fruit()
                screen.update()





if __name__ == "__main__":
    main()
    

