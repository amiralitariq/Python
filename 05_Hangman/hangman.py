import random
import string
from words import words  

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user
    attempts = 6  # Number of incorrect guesses allowed

    while len(word_letters) > 0 and attempts > 0:
        print(f"\nYou have {attempts} attempts left.")
        print("Used letters: ", ' '.join(used_letters))

        # Display current word progress
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:  # New valid letter guessed
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                attempts -= 1  # Wrong guess, lose an attempt
                print("Incorrect guess!")

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Please enter a valid letter.")

    # Game result
    if len(word_letters) == 0:
        print(f"\nCongrats! You guessed the word: {word} 🎉")
    else:
        print(f"\nYou lost! The correct word was: {word} ❌")

# Run the game
hangman()
