import random

def guess(low,high):
    random_number=random.randint(low,high)
    guess=0
    while guess!=random_number:
        guess=int(input("Guess a number: "))
        if guess<random_number:
            print("Sorry, guess again... The guess is low.")
        elif guess>random_number:
            print("Sorry, guess again... Your guess is high.")
    print(f"\nWooo Hoooo! You guessed the right number.\nThe number: {random_number}.\n\n")

n='y'
while(True):
    if n=='y':
        low=int(input("Enter the lower limit for the guessing game: "))
        high=int(input("Enter the upper limit of the guessing game: "))
        guess(low, high)
    else:
        exit(0)
    n=input("Enter 'y' if wanna play, else 'n' to exit: ")