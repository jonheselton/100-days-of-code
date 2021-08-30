##!/usr/bin/python
from turtle import Screen, Turtle

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
            x = x + 20
            self.segments.append(segment)

    def forward(self):
        for i in range(len(self.segments)-1, -1, -1):
            if i > 0:
                self.segments[i].goto(self.segments[i-1].position())
            else:
                self.segments[i].fd(20)

    def left(self):
        self.segments[0].left(90)

def main():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    game = Snake()
    game.snake()
    screen.update()
    game.forward()
    screen.update()
    game.forward()
    screen.update()
    game.forward()
    screen.update()
    game.left()
    screen.update()
    game.forward()
    screen.update()
    game.forward()
    screen.update()
    game.forward()
    screen.update()


    screen.exitonclick()

if __name__ == "__main__":
    main()
    

