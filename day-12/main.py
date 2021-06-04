import random

ANSWER = random.randint(0, 100)


def guess_a_number(guess, lives):
    global ANSWER
    if lives == 0:
        print('you lose')
        return
    else:
        lives += -1
    if guess == ANSWER:
        print('You Win!')
    elif guess > ANSWER:
        guess = int(input('Too High, Guess again'))
        return guess_a_number(guess, lives)
    elif guess < ANSWER:
        guess = int(input('Too Low, Guess again'))
        return guess_a_number(guess, lives)


def main():
    difficulty = input('choose a difficulty, easy, medium, hard: ')
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'medium':
        lives = 8
    else:
        lives = 5
    initial_guess = int(input('Guess the number! '))
    guess_a_number(initial_guess, lives)


if __name__ == "__main__":
    main()
