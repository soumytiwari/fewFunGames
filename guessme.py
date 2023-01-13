import random

def computer_guess(low,high):
    feedback=''
    while feedback!='c':
        if low!=high:
            computer_guess=random.randint(low, high)
        else:
            computer_guess=low
        print(f"Is the number... {computer_guess}???")
        feedback=input("Enter 'H' if high guess, 'L' if low guess, 'C' if correct guess___").lower()
        if feedback=='h':
            high=computer_guess-1
        elif feedback=='l':
            low=computer_guess+1
    print("\nYeeeyyy.... You are right sweety.\n\n")

n='y'
while(True):
    if n=='y':
        low=int(input("Enter lower limit for the game: "))
        high=int(input("Enter upper limit for the game: "))
        computer_guess(low,high)
    else:
        exit(0)
    n=input("Enter 'y' if you wanna play more, else 'n': ")