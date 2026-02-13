import random

def play_guessing_game():
    randomnumber = random.randint(1, 25)
    guess = 0
    attempts = 0

    print("Welcome to the (good code) Guessing Game !!!")
    print("\nA number has been chosen randomly between 1 and 25! You have 25 guesses and good luck!")

    while guess != randomnumber:
        try:
            guess = int(input("\nGuess a number between 1 and 25: "))
            attempts += 1

            if guess < randomnumber:
                print("\nToo low, try again!")

            elif guess > randomnumber:
                print("\nToo high, try again!")


        finally:
            if attempts > 25:
                print("\nYou have ran out of attempts")
                print("\nThe number was " + str(randomnumber))


