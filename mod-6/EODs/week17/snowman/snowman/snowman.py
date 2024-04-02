from random import choice
from stages import snowman
from logo import logo
import os

# get game word
def get_game_word():
    """reads the words file, strips away new lines and turns it to a list"""
    f = open("words.txt", "r")
    words = [ x.rstrip() for x in f]
    return choice(words)

# Printer helper
def printer(snowman, display, guesses, chances, error=None):
    if error:
        print(error)    
    print(snowman[chances])
    print(' '.join(display))
    if guesses:
        print(f"You have guessed: {guesses}")


def play_snowman():
    os.system('clear')
    print(logo)
    print('Welcome to Snowman!')
    print("♫♬ DO YOU WANT TO MELT A SNOWMAN!!! ♬♫")
    print("Guess the word before the snowman melts!")
    game_word = get_game_word()
    display = [ "_" for x in range(len(game_word))]
    chances = 0
    guesses = set()
    printer(snowman, display, guesses, chances)
    # print(snowman[chances])
    # print(' '.join(display))

    play = True
    while play:
        guess = input("Guess a letter: ").lower()
        os.system('clear')
        
        if guess in display or guess in guesses:
            error = f"You already guessed {guess.upper()}, try again, no penalty"
            printer(snowman, display, guesses, chances, error)
            # print(snowman[chances])
            # print(' '.join(display))
            # print(f"You have guessed: {guesses}")
            continue

        if guess not in "abcdefghijklmnopqrstuvwxyz":
            error = f"You can only guess letters, try again, no penalty"
            printer(snowman, display, guesses, chances, error)
            continue

        guesses.add(guess.upper())

        for index, letter in enumerate(game_word):
            if letter == guess:
                display[index] = letter.upper()


        if guess not in game_word:
            chances += 1
            print(f"Sorry, {guess.upper()} is not in the word...")
            if chances == 6:
                os.system("clear")
                print(snowman[-1])
                play = False
                print(f"YOU LOSE! The word was {game_word.upper()}.  POOR FROSTY... 💧")
                return    

        printer(snowman, display, guesses, chances)
        # print(' '.join(display))
        # print(f"You have guessed: {guesses}")
        # print(snowman[chances])

        if "_" not in display:
            play = False
            print(f"{game_word.upper()} was the word! YOU WIN! FROSTY LIVES!")
            return

play_snowman()