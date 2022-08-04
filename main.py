from art import logo

def caesar(text, shift, direction):
    encode_message = ""
    last_index = len(alphabet) - 1
    shift_amount = shift % last_index
    if direction == "decode":
            shift_amount *= -1
    for letter in text:
        if letter not in alphabet:
            encode_message += letter
        else:
            position = alphabet.index(letter) + shift_amount
            if position > last_index:
                position -= last_index + 1
            encode_message += alphabet[position]
    print(f"Here's the {direction}d result: {encode_message}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
play = True
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    resume= input("Type 'yes' with you want to go again, otherwise type 'no': ").lower()
    if resume != "yes":
        play = False
print("Goodbye o/")