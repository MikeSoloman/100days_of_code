from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(directions, plain_text, amount_shift):
    while True:
        if amount_shift > 26:
            amount_shift = amount_shift % 26
        end_text = ""
        if directions == "decode":
            amount_shift *= -1
        for letter in plain_text:
            if letter.isalpha():
                position = alphabet.index(letter)
                new_position = position + amount_shift
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(f"The {directions} text is {end_text}")

        ask_question = input("Would you like to try again? y/n? ").lower()
        if ask_question == 'n':
            break
        else:
            directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            plain_text = input("Type your message:\n").lower()
            amount_shift = int(input("Type the shift number:\n"))

print(caesar(direction, text, shift))
