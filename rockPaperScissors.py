import random

def play():
    computer_choice=random.choice(['rock', 'paper', 'scissors'])
    user_choice=input("Make your choice: ").lower()
    if computer_choice==user_choice:
        return "It's a tie."
    if win_situation(computer_choice, user_choice):
        return "You Won!"
    return "You Lost!"

def win_situation(computer_choice, user_choice):
    if (user_choice=="rock" and computer_choice=="scissors") or (computer_choice=="rock" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="scissors"):
        return True


print("\n\t\t-----------------      Rock, Paper, Scissors       ---------------------\n")
while(True):
    inputt=input("Wanna play? ").lower()
    if inputt=="yes":
        print(play())
    else:
        exit(0)