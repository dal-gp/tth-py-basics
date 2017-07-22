# TODO
# Limit the number of guesses
# Catch when someone submits a non-integer
# Print "too low" or "too high msgs for bad gueses
# Let people play again

import random


def game():
    # generate a random number between 1 and 10

    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        guess = 0
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} is not a number".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            else:
                print("That's not it!")
            guesses.append(guess)
    else:
        print("You didnot get it! My number was {}".format(secret_num))

game()
