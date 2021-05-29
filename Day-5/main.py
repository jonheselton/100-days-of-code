# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def random_character(character, quantity):
    rand = []
    if character == "letters":
        while quantity > 0:
            rand.append(letters[random.randint(0, 51)])
            quantity = quantity - 1
        return rand
    elif character == "numbers":
        while quantity > 0:
            rand.append(numbers[random.randint(0, 9)])
            quantity = quantity - 1
        return rand
    elif character == "symbols":
        while quantity > 0:
            rand.append(symbols[random.randint(0, 8)])
            quantity = quantity - 1
        return rand


pwd_letters = random_character('letters', nr_letters)
pwd_numbers = random_character('numbers', nr_numbers)
pwd_symbols = random_character('symbols', nr_symbols)
pwd_notrandomized = pwd_symbols + pwd_letters + pwd_numbers
final_pwd = ''
while len(pwd_notrandomized) > 0:
    final_pwd += pwd_notrandomized.pop(random.randint(0, len(pwd_notrandomized)-1))
print(final_pwd)


