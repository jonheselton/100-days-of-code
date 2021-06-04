##!/usr/bin/python
from game_data import data
import random


def choose():
    return random.randint(0, len(data))


def compare(object1, object2):
    if data[object1]['follower_count'] > data[object2]['follower_count']:
        return data[object1]
    else:
        return data[object2]


def main():
    choice1 = choose()
    choice2 = choose()
    print('Select option (1) or (2)')
    guess = int(input(data[choice1]['name'] + ' or ' + data[choice2]['name']))
    if guess == 1:
        guess = choice1
    elif guess == 2:
        guess = choice2
    else:
        return
    correct_answer = compare(choice1, choice2)
    if data[guess] == correct_answer:
        keep_playing = True
    else:
        print('you lose')
        return
    while keep_playing:
        choice1 = guess
        choice2 = choose()
        print('Select option (1) or (2)')
        guess = int(input(data[choice1]['name'] + ' or ' + data[choice2]['name']))
        if guess == 1:
            guess = choice1
        elif guess == 2:
            guess = choice2
        else:
            return
        correct_answer = compare(choice1, choice2)
        if data[guess] == correct_answer:
            keep_playing = True
        else:
            print('you lose')
            return



if __name__ == "__main__":
    main()
