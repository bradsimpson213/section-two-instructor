# GUESSING GAME

# Things we will need...
# 1. random - generate random numbers - X
# 2. user input - X
# 3. iterating - X
# 4. guess tracker - number of guesses - X
# 5. conditionals - X
# 6. helper function - X
from random import randint

# GUESS helper function
def guess(start, end):
    bad_guess = True
   
    while bad_guess:
        try:
            user_input = int(input(f"Pick a number from {start} to {end}: "))
        except ValueError:
            print("We need to enter numbers for the guessing game!")
            continue
        else: 
            if user_input < start or user_input > end:
                print(f"Numbers need to be from 1 to 20, not {user_input}")
                continue
   
        bad_guess = False
    return user_input


def guessing_game():
    print("Welcome to the guessing game!")
    start = 1
    end = 50
    winning_number = randint(start, end)
    guesses = 5

    while guesses > 0:
        user_guess = int(input(f"Pick a number from {start} to {end}: "))
        # user_guess = guess(start, end) 
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed it!  The number was {winning_number}!  You used {5 - guesses} to win! Yay!")
            return
        
        elif user_guess > winning_number:
            print(f"You guessed too high!  Try again!  You have {guesses} guesses left!")

        else:
            print(f"You guessed too low!  Try again!  You have {guesses} guesses left!")


    print(f"You ran out of guesses.  So sorry you lost. The number was {winning_number}")

guessing_game()

















from random import randint

# Notes
# 1. user input
# 2. loop
# 3. number of guesses
# 4. generate a random number 
# 5. conditionals

def guess(start, end):
    bad_guess = True
    user_input = None
   
    while bad_guess:
        try:
            user_input = int(input(f"Pick a number from {start} to {end}: "))
        
        except ValueError:
            print("We need to enter numbers for the guessing game!")
            continue

        else: 
            if user_input < start or user_input > end:
                print(f"Numbers need to be from 1 to 20, not {user_input}")
                continue
        
   
        bad_guess = False
    
    return user_input



def guessing():
    print("Welcome to the guessing game!")
    start = 1
    end = 20
    winning_number = randint(start, end)
    guesses = 5

    while guesses > 0:
        # user_guess = int(input("Pick a number from 1 to 20: "))    
        user_guess = guess(start, end) 
        guesses -= 1
   
        if user_guess == winning_number:
            print(f"You guessed correctly!  The number was {winning_number}")
            # add fun conditional for a sniper
            return
        elif user_guess > winning_number:
            print(f"You guessed to high!  Try again!  You have {guesses} guesses left")
        else:
            print(f"You guessed to low!  Try again!  You have {guesses} guesses left")

    print(f"You are out of guesses.  You lose.  The number was {winning_number}")


guessing()



from random import randint


def guess(start, end):
    bad_guess = True

    while bad_guess:
        try:
            user_guess = int(input(f"Pick a number from {start} to {end}: "))
        
        except ValueError:
            print("We need to enter numbers not strings to play the game")
            continue

        else:
            if user_guess < start or user_guess > end:
                print(f"Numbers need to be in the range of {start} and {end}, you picked {user_guess}")
                continue


        bad_guess = False

    return user_guess


def guessing_game():
    print("Welcome to the guessing game!")
    guesses = 5
    start = 1
    end = 20
    winning_number = randint(start, end)

    while guesses > 0:
        # user_guess = int(input(f"Pick a number from {start} to {end}: "))
        user_guess = guess(start, end)
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed correctly!  The number was {winning_number}")
            return
        
        elif user_guess > winning_number:
            print(f"You guessed to high!  Try again!  You have {guesses} guesses left!")

        else:
            print(f"You guessed to low!  Try again!  You have {guesses} guesses left!")

    print(f"You are out of guesses.  Game over! The number was {winning_number}")


guessing_game()


from random import randint

# Notes
# 1. user input
# 2. loop
# 3. number of guesses
# 4. generate a random number 
# 5. conditionals

def guessing():
    print("Welcome to the guessing game!")
    winning_number = randint(1, 20)
    guesses = 5

    while guesses > 0:
        user_guess = int(input("Pick a number from 1 to 20: "))     
        guesses -= 1
   
        if user_guess == winning_number:
            print(f"You guessed correctly!  The number was {winning_number}")
            return
        elif user_guess > winning_number:
            print(f"You guessed to high!  Try again!  You have {guesses} guesses left")
        else:
            print(f"You guessed to low!  Try again!  You have {guesses} guesses left")

    print(f"You are out of guesses.  You lose.  The number was {winning_number}")


guessing()

