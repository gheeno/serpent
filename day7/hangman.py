"  Hangman game  "

import random

word_list = ["aardvark", "baboon", "camel"]


def random_word_picker(arg):
    """ Random list picker. """
    return random.choice(arg)


def list_the_word(random_word):
    " List a param. "
    return list(random_word)


def empty_list_maker(_word_list):
    " Create an empty list. "
    list_total = len(_word_list)
    count = 0
    _blank_list = []
    while count < list_total:
        _blank_list.append("_")
        count += 1
    return _blank_list


def list_updater(letter_param, list_1, list_2):
    " list 2 updater. "
    if letter_param in list_1:
        # TODO-1 - if multiple characters are present it's only present on the initial underscore.
        index = list_1.index(letter_param)
        list_2[index] = letter_param
    else:
        print("Sorry, that letter is not in the word.")
    return list_2

#Scoring 
# 1. each guessed letter, do not deduct health
# 2. if user makes a mistake, "seorry that letter is not in the word"
# 2a. deduct the health
# 3. Draw hangman every failure.

if __name__ == "__main__":
    rand_word = random_word_picker(word_list)
    print(f"the random word : '{rand_word}'")
    _list = list(rand_word)
    print(f"the random word as list \n{_list}")
    _hidden_list_val = []
    _hidden_list_val = empty_list_maker(_list)
    while _list != _hidden_list_val:
      guessed_letter = input("Guess a letter: ").lower()
      _hidden_list_val = list_updater(guessed_letter, _list,
                                        _hidden_list_val)
      print(_hidden_list_val)
