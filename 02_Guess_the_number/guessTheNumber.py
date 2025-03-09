import random

def guess(x):
    random_number = random.randint(1,x)
    name = input('Enter your name: ')
    count=0
    guess = 0
    while guess!=random_number:
        guess = int (input(f"Guess a number between 1 and {x} = "))
        if guess == 0:
            print("Don't enter 0, try again!")
        elif guess<random_number:
            count+=1
            print("Sorry, guess again, Too Low")
        elif guess>random_number:
            count+=1
            print("Sorry, guess again, Too high")
        else:
            print(f"Congratulations! Your guess is correct. {name} you made a correct guess in {count}")

guess(10)