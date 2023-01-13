from sampleMadlib import loveLetter, dragon, deathStar, inTheSky, madlibTry, superHero
import random

while (True):
    print("Input 'y' to continue 'n' to exit.")
    inputt=input("Enter your choice: ")
    if inputt=="y":
        if __name__ =="__main__":
            r=random.choice([loveLetter, dragon, deathStar, inTheSky, madlibTry, superHero])
            r.madlib()
    else:
        exit(0)