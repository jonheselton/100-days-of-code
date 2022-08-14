import turtle
import pandas

class Game:
    def __init__(self) -> None:
        self.data = pandas.read_csv('50_states.csv')
        self.background = 'blank_states_img.gif'
        self.score = 0
        self.pen = turtle.Turtle()
        self.pen.color('black')
        self.pen.pu()
        self.answers_remaining = self.data.state.to_list()
    def check_answer(self, answer):
        if 1 == len(self.data[self.data.state == answer.title()]):
            self.score = self.score + 1
            x_cord = int(self.data[self.data.state == answer.title()].x)
            y_cord = int(self.data[self.data.state == answer.title()].y)
            self.pen.setx(x_cord)
            self.pen.sety(y_cord)
            self.pen.write(answer.title())
            self.answers_remaining.pop(self.answers_remaining.index(answer.title()))
        else:
            return False