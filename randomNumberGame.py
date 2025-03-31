'''
#* = TASK COMPLETED
Random Number Game:
#* 1) Shows CLI UI and Displays Game Name + Rules (Number from 1 - 100)
#* 2) User Chooses Difficulty (Easy, Medium, Hard). Difficulty changes number of tries
#* 3) Good luck message.
#* 4) Game Starts
#* 5) When User Guesses, It will say if the number is less than or greater than the random number
#* 6) If the user is correct, Congratulatory Message will appear alongside the number of attempts used to win
#* 7) If the user loses, say you have lost and display the random number.
'''
# Importing tools. Random allows random integers, sys allows a better exit
import random
import sys

def Menu():
    print('{:^70s}'.format("~~~~~~~~~~~~~~~~~~~~~~~"))
    print('{:^70s}'.format("Random Number Guesser"))
    print('{:^70s}'.format("~~~~~~~~~~~~~~~~~~~~~~~"))

    print("\n" '{:^70s}'.format("Rules:"))
    print('{:^70s}'.format("A Random Number from 1-100 will be Chosen"))
    print('{:^70s}'.format("Your Job is to Guess the Number without Running Out of Lives!"))
    
    Game()

def Game():
    print("\n" '{:^70s}'.format("Which Difficulty Would you like to Choose?"))
    print('{:^70s}'.format("[1] Easy (10 Guesses) "))
    print('{:^70s}'.format("[2] Normal (5 Guesses)"))
    print('{:^70s}'.format("[3] Hard (3 Guesses)  "))

    # While loop and try. Try and except allows the user to retry if there is a ValueError (not an integer as defined)
    while True:
        try:
            choice = int(input())
            if choice == 1:
                difficulty = 'Easy'
                break
            if choice == 2:
                difficulty = 'Normal'
                break
            if choice == 3:
                difficulty = 'Hard'
                break
            if choice > 3 or choice < 1:
                print("This input is invald. Please try again\n")
                continue
        except ValueError:
            print("This input is invald. Please try again\n")
            continue

    # Difficulty being set. This changes the amount of guesses
    if difficulty == 'Easy':
        guessRemain = 10
    if difficulty == 'Normal':
        guessRemain = 5
    if difficulty == 'Hard':
        guessRemain = 3
    
    print('{:^70s}'.format("You Have Chosen " + difficulty + " Difficulty"))
    print('{:^70s}'.format("Good Luck!"))

    randomInt = random.randint(1, 100)

    print("\n" '{:^70s}'.format("A Random Number has been Picked\n"))
    print('{:^70s}'.format("Start Guessing!\n"))
    guessAmount = 0

    while True:
        try:
            guess = int(input(""))
            if guess != randomInt:
                print("Incorrect.", guess, "is > the Random Number" if guess > randomInt else "is < the Random Number")
                guessRemain = guessRemain - 1
                guessAmount = guessAmount + 1
                if guessRemain == 0:
                    print("\n", '{:^70s}'.format("You Have Failed! The correct number was %d\n") %randomInt)
                    break
                continue
            if guess == randomInt:
                guessAmount = guessAmount + 1
                print("\n" + '{:^70s}'.format("Congratulations! The number was indeed %d") %randomInt)
                print('{:^70s}'.format("This took you %d Guesses!\n") %guessAmount)
                break
        except ValueError:
            print("This input is invald. Please try again")

    while True:
        retry = input("Would you like to Retry? Y/n ")
        if retry == "" or retry.lower() == "y":
            Game()
            break
        elif retry.lower() == "n":
            sys.exit()
        else:
            print("This input is invald. Please try again")
            continue

# Opens functions if a function is left or the code is started. Otherwise the code will skip everything since they are in functions
Menu()
Game()