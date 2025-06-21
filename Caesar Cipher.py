# TODO-1: Import and print the logo from art.py when the program starts.
# Test OK.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1  # If the problem is that the value keeps flipping on and off negative, maybe I need to look outside.
    # Seems like my intuition was on the mark. The negative was being looped as well which ruined the decode process. Now that I've removed it, it works every time.


    for letter in original_text:


        if letter not in alphabet:
            output_text += letter
        # TODO-2: What happens if the user enters a number/symbol/space?
        # It retains those things.
        # Test OK.


        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]


    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


program_end = False

while not program_end:
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    redo = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if redo == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))


    if redo == "no":
        program_end = True
# Needs work. Still haven't quite figured out how to loop the program without the decode messing up.
