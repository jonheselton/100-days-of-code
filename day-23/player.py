from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
       super().__init__()
       self.color('green')
       self.pu()
       self.setpos(STARTING_POSITION)
       self.seth(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def score(self):
        if self.ycor() >= 300:
            self.player_reset()
            return True
        else:
            return False

    def player_reset(self):
        self.setpos(STARTING_POSITION)
