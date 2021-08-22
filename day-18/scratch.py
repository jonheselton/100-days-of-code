##!/usr/bin/python

from turtle import Turtle
from turtle import Screen
from random import randint
from random import choice


def main():
    turtle = Turtle()
    turtle.pensize(5)
    turtle.speed(10000)
    turtle.shape("circle")
    turtle.pu()
    turtle.setposition(-255, -255)
    screen = Screen()
    screen.screensize(255, 255)
    screen.colormode(255)
    for x in range(-16, 16):
        for y in range(-16, 16):
            red = randint(1, 255)
            green = randint(1, 255)
            blue = randint(1, 255)
            color = (red, green, blue)
            turtle.pencolor(color)
            turtle.setposition(x*16, y*16)
            turtle.fillcolor(color)
            turtle.stamp()





    #for n in range(0, 360):


    screen.exitonclick()
#    for _ in range(0, 10):
#        turtle.forward(10)
#        turtle.penup()
#        turtle.forward(10)
#        turtle.pendown()



if __name__ == "__main__":
    main()
