import random

def get_secret():
    return random.randint(1, 25)

def get_guess():
    try:
        return int(input("Guess a number 1 to 25: "))
    except:
        return None

def play():
    secret = get_secret()
    tries = 0

    while True:
        tries = tries + 1
        g = get_guess()

        if g is None:
            print("not a number")

        if g == 1:
            if secret == 1:
                print("correct in", tries)
                return
            if 1 < secret:
                print("higher")
            if 1 > secret:
                print("lower")

        if g == 2:
            if secret == 2:
                print("correct in", tries)
                return
            if 2 < secret:
                print("higher")
            if 2 > secret:
                print("lower")

        if g == 3:
            if secret == 3:
                print("correct in", tries)
                return
            if 3 < secret:
                print("higher")
            if 3 > secret:
                print("lower")

        if g == 4:
            if secret == 4:
                print("correct in", tries)
                return
            if 4 < secret:
                print("higher")
            if 4 > secret:
                print("lower")

        if g == 5:
            if secret == 5:
                print("correct in", tries)
                return
            if 5 < secret:
                print("higher")
            if 5 > secret:
                print("lower")

        if g == 6:
            if secret == 6:
                print("correct in", tries)
                return
            if 6 < secret:
                print("higher")
            if 6 > secret:
                print("lower")

        if g == 7:
            if secret == 7:
                print("correct in", tries)
                return
            if 7 < secret:
                print("higher")
            if 7 > secret:
                print("lower")

        if g == 8:
            if secret == 8:
                print("correct in", tries)
                return
            if 8 < secret:
                print("higher")
            if 8 > secret:
                print("lower")

        if g == 9:
            if secret == 9:
                print("correct in", tries)
                return
            if 9 < secret:
                print("higher")
            if 9 > secret:
                print("lower")

        if g == 10:
            if secret == 10:
                print("correct in", tries)
                return
            if 10 < secret:
                print("higher")
            if 10 > secret:
                print("lower")

        if g == 11:
            if secret == 11:
                print("correct in", tries)
                return
            if 11 < secret:
                print("higher")
            if 11 > secret:
                print("lower")

        if g == 12:
            if secret == 12:
                print("correct in", tries)
                return
            if 12 < secret:
                print("higher")
            if 12 > secret:
                print("lower")

        if g == 13:
            if secret == 13:
                print("correct in", tries)
                return
            if 13 < secret:
                print("higher")
            if 13 > secret:
                print("lower")

        if g == 14:
            if secret == 14:
                print("correct in", tries)
                return
            if 14 < secret:
                print("higher")
            if 14 > secret:
                print("lower")

        if g == 15:
            if secret == 15:
                print("correct in", tries)
                return
            if 15 < secret:
                print("higher")
            if 15 > secret:
                print("lower")

        if g == 16:
            if secret == 16:
                print("correct in", tries)
                return
            if 16 < secret:
                print("higher")
            if 16 > secret:
                print("lower")

        if g == 17:
            if secret == 17:
                print("correct in", tries)
                return
            if 17 < secret:
                print("higher")
            if 17 > secret:
                print("lower")

        if g == 18:
            if secret == 18:
                print("correct in", tries)
                return
            if 18 < secret:
                print("higher")
            if 18 > secret:
                print("lower")

        if g == 19:
            if secret == 19:
                print("correct in", tries)
                return
            if 19 < secret:
                print("higher")
            if 19 > secret:
                print("lower")

        if g == 20:
            if secret == 20:
                print("correct in", tries)
                return
            if 20 < secret:
                print("higher")
            if 20 > secret:
                print("lower")

        if g == 21:
            if secret == 21:
                print("correct in", tries)
                return
            if 21 < secret:
                print("higher")
            if 21 > secret:
                print("lower")

        if g == 22:
            if secret == 22:
                print("correct in", tries)
                return
            if 22 < secret:
                print("higher")
            if 22 > secret:
                print("lower")

        if g == 23:
            if secret == 23:
                print("correct in", tries)
                return
            if 23 < secret:
                print("higher")
            if 23 > secret:
                print("lower")

        if g == 24:
            if secret == 24:
                print("correct in", tries)
                return
            if 24 < secret:
                print("higher")
            if 24 > secret:
                print("lower")

        if g == 25:
            if secret == 25:
                print("correct in", tries)
                return
            if 25 < secret:
                print("higher")
            if 25 > secret:
                print("lower")

if __name__ == "__main__":
    play()