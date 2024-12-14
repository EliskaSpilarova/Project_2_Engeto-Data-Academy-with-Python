"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Eliška Špilarová
email: eliska.spilarova@gmail.com
"""
import random

def create_number():
    while True:
        number = random.sample('1234567890', 4)  
        if number[0] != '0':  
            return ''.join(number)

def is_valid_input(user_input):
    if len(user_input) != 4:  
        return False
    if not user_input.isdigit():  
        return False
    if len(set(user_input)) != 4:  
        return False
    if user_input[0] == '0':  
        return False
    return True

def play_bulls_cows(inserted, required):
    bulls = 0
    cows = 0
    for i in range(4):
        if inserted[i] == required[i]:
            bulls += 1
        elif inserted[i] in required:
            cows += 1
    return bulls, cows

def format_bulls_cows(bulls, cows):
    if bulls == 1:
        bull_text = "1 bull"
    else:
        bull_text = f"{bulls} bulls"
    
    if cows == 1:
        cow_text = "1 cow"
    else:
        cow_text = f"{cows} cows"
    
    return bull_text, cow_text

required_number = create_number()  

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")
print("Enter a number:")
print("-----------------------------------------------")

guess_count = 0

while True:
    user_input = input(">>> ")

    if not is_valid_input(user_input):
        print("Invalid input. Please make sure your number:")
        print("- is exactly 4 digits long")
        print("- contains only digits")
        print("- has no repeated digits")
        print("- does not start with 0")
        continue

    bulls, cows = play_bulls_cows(user_input, required_number)
    
    bull_text, cow_text = format_bulls_cows(bulls, cows)
    
    print(f"{bull_text}, {cow_text}")
    print("-----------------------------------------------")
    
    guess_count += 1
    
    if bulls == 4:
        print(f"Correct, you've guessed the right number in {guess_count} guesses!")
        print("That's amazing!")
        break
