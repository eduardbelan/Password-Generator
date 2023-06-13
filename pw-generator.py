# Password Generator Project
import random
import os
import sys

from art import logo


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def clear_screen():
    """
    Clear the console for Windows or Linux
    """
    # Windows
    clear = lambda: os.system("cls")
    clear()
    # Linux
    # clear = lambda os.system("clear")
    # clear()


clear_screen()
print(logo)
print("Welcome to the PyPassword Generator!")
print("You can choose how many:"
      "\n\t- letters"
      "\n\t- symbols"
      "\n\t- numbers"
      "\n\t- secret words"
      "\nyour Password should contain.\n")


# Number of Letters, Symbols & Numbers
while True:
    try:
        nr_letters = int(input("How many letters would you like? "))
        break
    except ValueError:
        print("\tPlease enter numbers only.")
print("")
while True:
    try:
        nr_symbols = int(input(f"How many symbols would you like? "))
        break
    except ValueError:
        print("\tPlease enter numbers only.")
print("")
while True:
    try:
        nr_numbers = int(input(f"How many numbers would you like? "))
        break
    except ValueError:
        print("\tPlease enter numbers only.")
print("")

characters = []
for i in range(nr_letters):
    random_letter = random.choices(letters)
    characters.append(random_letter[0])
for i in range(nr_symbols):
    random_symbol = random.choices(symbols)
    characters.append(random_symbol[0])
for i in range(nr_numbers):
    random_number = random.choices(numbers)
    characters.append(random_number[0])


# Number of Secret Words
while True:
    try:
        num_words = int(input("How many secret words would you like? "))
        if num_words > 10:
            print("\tThe maximum amount of secret words is 10.\n")
        else:
            break
    except ValueError:
        print("\tPlease enter numbers only.\n")

secret_words = []
for i in range(num_words):
    if i == 0:
        ordinal = "st"
    elif i == 1:
        ordinal = "nd"
    elif i == 2:
        ordinal = "rd"
    else:
        ordinal = "th"

    word = input(f"Enter the {i+1}{ordinal} secret word: ")
    # Remove all empty spaces
    word = ''.join(word.split())
    secret_words.append(word)


# Order not randomised
print("\nOrder not randomised.")
print(f"Your Password: {''.join(characters)}{''.join(secret_words)}")


# Order randomised
# Join the lists
chars_words = characters + secret_words
# Randomise the list
random.shuffle(chars_words)

print("\nOrder randomised.")
print(f"Your Password: {''.join(chars_words)}\n")


# Overview
print(f"Your Password contains:"
      f"\n\t{nr_letters} letters: {', '.join(characters[:nr_letters])}"
      f"\n\t{nr_symbols} symbols: {', '.join(characters[nr_letters:nr_letters+nr_symbols])}"
      f"\n\t{nr_numbers} numbers: {', '.join(characters[nr_letters+nr_symbols:])}")
if not secret_words:
    print(f"It contains {num_words} secret words.\n")
else:
    print(f"It also contains {num_words} secret words: {', '.join(secret_words)}\n")


# Determine Password Strength
if nr_letters == 0 and nr_numbers == 0:
    print("Password contains only Symbols.\n"
          "Password is not safe.")
elif nr_letters == 0 and nr_symbols == 0:
    print("Password contains only Numbers.\n"
          "Password is not safe.")
elif nr_numbers == 0 and nr_symbols == 0:
    print("Password contains only Letters.\n"
          "Password is not safe.")
elif nr_letters == 0:
    print("Password contains no letters.\n"
          "Password is not safe.")
elif nr_numbers == 0:
    print("Password contains no Numbers.\n"
          "Password is not safe.")
elif nr_symbols == 0:
    print("Password contains no Symbols.\n"
          "Password is not safe.")
else:
    print("Password is safe.")

# Exit the program
valid_input = False

while not valid_input:
    exit_program = input("\nPress X to quit: ").lower()

    if exit_program == "x":
        clear_screen()
        sys.exit()
