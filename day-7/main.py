
import random
from wordlist import word_list
import hangman_art

# Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
# Import the stages from hangman_art.py and make this error go away.
# Import the logo from hangman_art.py and print it at the start of the game.
# If the user has entered a letter they've already guessed, print the letter and let them know.
# If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.


def display(input_word):
    blanks = []
    nr_blanks = len(input_word)
    for i in range(0, nr_blanks):
        blanks.append('_')
    return blanks


# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
print(word)
# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
# the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
# guess.
print(hangman_art.logo)
displayed_word = display(word)


# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
guessed = []
while displayed_word.count('_') > 0 and lives > 0:
    valid_guess = False
    while not valid_guess:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        guess = input("Please choose a letter! ").lower()
        if guess in guessed:
            print('you already chose '+guess)
            print('guess again')
        else:
            valid_guess = True
        # Loop through each position in the chosen_word;
        # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p",
    j = 0
    round_won = False
    for letter in word:
        if letter == guess:
            displayed_word[j] = guess
            j += 1
            round_won = True
            guessed += guess
        else:
            guessed += guess
            j += 1
    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace
    # with "_".
    print(displayed_word)

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if not round_won:
        lives += -1
        print(hangman_art.stages[lives])
        print('{} was not in the word'.format(guess))
        print('You have {} remaining'.format(lives))
if lives == 0:
    print("you lose!q")
else:
    print("you win!")

