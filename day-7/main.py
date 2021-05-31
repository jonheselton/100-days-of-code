# #!/usr/bin/env python
import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
print(word)


# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
# the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
# guess.

def display(word):
    blanks = []
    nr_blanks = len(word)
    for i in range(1, nr_blanks):
        blanks.append('_')
    return blanks


displayed_word = display(word)

print(displayed_word)
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please choose a letter! ").lower()

# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p",
i = 0
for letter in word:
    if letter == guess:
        displayed_word[i] = guess
        i += 1
    else:
        i += 1

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(displayed_word)