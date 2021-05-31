# Import and print the logo from art.py when the program starts.
# What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
# What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"

# Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(string, number, direction):
    if number // 26 > 0:
        number = number -((number // 26)*26)
    if direction == 'encode':
        encrypted_string = ''
        for letter in string:
            if letter.isalpha():
                encoded_letter = alphabet.index(letter) + number
                if encoded_letter > 25:
                    encoded_letter += -25
                encrypted_string += alphabet[encoded_letter]
            else:
                encoded_letter = letter
                encrypted_string += letter

        return encrypted_string
    elif direction == 'decode':
        decrypted_string = ''
        for letter in string:
            decoded_letter = alphabet.index(letter) - number
            if decoded_letter < 0:
                decoded_letter += 25
            decrypted_string += alphabet[decoded_letter]

        return decrypted_string


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(string, number):
    # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and
    # print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output: "The encoded
    # text is mjqqt"
    encrypted_string = ''
    for letter in string:
        encoded_letter = alphabet.index(letter) + number
        if encoded_letter > 25:
            encoded_letter += -25
        encrypted_string += alphabet[encoded_letter]

    return encrypted_string
    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(string, number):
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    decrypted_string = ''
    for letter in string:
        decoded_letter = alphabet.index(letter) - number
        if decoded_letter < 0:
            decoded_letter += 25
        decrypted_string += alphabet[decoded_letter]

    return decrypted_string


# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


def main():
    play = True
    while play:
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        # Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
        # message.
        print(caesar(text, shift, direction))
        play_again = input("Play again? y/n ")
        if play_again != 'y':
            play = False


if __name__ == "__main__":
    main()
