import random

def play_guessing_game():
    randomnumber = random.randint(1, 25)
    guess = 0
    attempts = 0

    print("Welcome to the (good code) Guessing Game !!!")
    print("A number has been chosen randomly between 1 and 25! You have unlimited guesses and good luck!")

