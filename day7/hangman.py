"Hangman game"

import random

word_list = ["aardvark", "baboon", "camel"]

def random_word_picker(arg):
    """ Random list picker. """
    return random.choice(arg)

def get_guess_letter():
    """ Input, save guessed letter. """
    while True:
        guessed_letter = input("Guess a letter: ").lower()
        if len(guessed_letter) == 1:
            return guessed_letter
        print("Please enter a single letter.")

def letter_checker(letter, random_word):
    """ Boolean : if letters in the list, return true. """
    letter_list = list(random_word)
    for i in letter_list:
        if i == letter:
            print("Right")
        else:
            print("Wrong")


def list_printer(_letter, _word):
    """ Hangman list printer. """
    _list = list(_word)
    print(_list)
    list_len = len(_list)
    count = 0
    while count < list_len:
        if not _list[count] == _letter:
            _list[count] = "_"
        count = count + 1
    print(_list)


if __name__ == "__main__":
    i = random_word_picker(word_list)
    print(f"the random word : {i}")
    letter = get_guess_letter()
    list_printer(letter, i)
