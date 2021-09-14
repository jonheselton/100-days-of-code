from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.setpos(-280, 250)
        self.level = 1
        self.write('LEVEL: ' + str(self.level), font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write('LEVEL: ' + str(self.level), font=FONT)

    def you_lose(self):
        self.setpos(0, 0)
        self.write('You Lose!')