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
            elif guess < secret_num:
                print("My number is higher than {}.".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        # This else will run when while loops ends
        # and when break and exceptions does not happen
        print("You did not get it! My number was {}".format(secret_num))

    play_again = input("Do you want to play again? ")
    if play_again != 'n':
        game()
    else:
        print("BYE!")

game()
