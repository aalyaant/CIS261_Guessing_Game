#Alyce Gaines
#CIS261
#Guessing Game

import random

#init vars
continuePlay = "y"

def play(limitNum):
    tryCount = 0
    print(f"I'm thinking of a number from 1 to {limitNum}\n")
    randomNum = random.randint(1, limitNum)
    guessNum = int(input("Your Guess: "))
    while(guessNum != randomNum):
        if guessNum<randomNum:
            print("Go Higher!")
            tryCount += 1
        elif guessNum>randomNum:
            print("Little Lower!")
            tryCount += 1
        guessNum = int(input("Your Guess: "))
    print(f"Good Job! You Guessed It In {tryCount}!")


#entry
def main():
    print("Guess the Number!")
    global continuePlay

    while continuePlay.lower() == "y":
        limitNum = int(input("Enter the limit: "))
        play(limitNum)
        continuePlay = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()