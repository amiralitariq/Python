import random
import string
from words import words

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    user_letter = input('Guess a letter').upper()

    if user_letter in alphabet


    user_input = input('Guess a letter: ').upper()

