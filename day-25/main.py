import turtle
import pandas
from game import Game

img_path = 'blank_states_img.gif'

wrong_guesses = 0
game = Game()
screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(img_path)
turtle.shape(img_path)
while wrong_guesses < 3:
    answer = screen.textinput('%s correct' % game.score, 'Guess a state:')
    if game.check_answer(answer) == False:
        wrong_guesses = wrong_guesses + 1
    screen.update()
print(game.answers_remaining)
screen.mainloop()