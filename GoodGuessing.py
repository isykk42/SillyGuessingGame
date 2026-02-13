import random

def play_guessing_game():
    randomnumber = random.randint(1, 25)
    guess = 0
    attempts = 0

    print("\nWelcome to the (good code) Guessing Game !!!")
    print("A number has been chosen randomly between 1 and 25! You have 25 guesses and good luck!")

    while guess != randomnumber and attempts < 25:
        try:
            guess = int(input("\nGuess a number between 1 and 25: "))
            attempts += 1

            if guess < randomnumber:
                print("Too low, try again!")

            elif guess > randomnumber:
                print("Too high, try again!")
        except ValueError:
            print("\nPlease enter a number between 1 and 25!")

    if guess == randomnumber:
        print(f"\nCongratulations! You guessed the number {randomnumber} in {attempts} attempts!")

    else:
        print("\nYou have ran out of attempts :(")
        print("The number was " + str(randomnumber))


    print("Thank you for playing!")

if __name__ == "__main__":
    play_guessing_game()
