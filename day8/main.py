alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

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

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(string, number):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
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
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
    if direction == 'encode':
        print(encrypt(text, shift))
    elif direction == 'decode':
        print(decrypt(text, shift))

if __name__ == "__main__":
    main()