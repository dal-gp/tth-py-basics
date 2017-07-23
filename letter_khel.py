# letter guess garnay game
# yo game le list bata random word chancha, ani hamilai letter guess garna lagaucha
# jaba samma hamilay right guess gardainau athawa  hamro chance siddincha
#
# TODOs:
# sabda ko list banaunay
# euta random word tyo list bata tipnay
# space draw garnay
# guess garnay
# guessed letters ra strikes(kati wata letter miss bhayeko bhanayra) draw garnay
# jityo ki haryo bhanayra output garnay

import random

words = [
    'syau',
    'kera',
    'suntala',
    'nariwal',
    'aamilo',
    'kharbuja'
]

while True:
    # surumai game quit garnay option dinay
    start = input("Press enter/return to start, or enter Q to quit")
    if start.lower() == 'q':
        break
    # random sabda pick garnay tyo lsit of words bata
    secret_word = random.choice(words)
    # yo duita list haru le user le input gareko guess store garcha.
    # yedi letter tyo secret_word ma chaina bhanay bhanay bad_guesses ma store garnay
    # natra yedi letter tyo secret_word ma cha bhanay good_guesses ma store garnay
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('-', end='')
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didn't guess it! My secret word was {}".format(secret_word))