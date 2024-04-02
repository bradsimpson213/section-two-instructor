# import stuff up here
from random import choice
from logo import logo
import os
from colorama import Back, Style


class Wordle:
    def __init__(self, letters=5, logo=logo):
        self.letters = letters
        self.logo = logo
        self.words = self.get_all_words()
        self.game_word = self.chose_game_word()
        print(self.game_word)
        self.guess = ''
        self.guesses = [[] for _ in range(6)]
        self.tries = 0
        self.play_game()        


    def get_all_words(self):
        f = open("words.txt", "r")
        words = [word.rstrip() for word in f]
        wordle_words = [ word for word in words if len(word) == self.letters]
        return wordle_words


    def chose_game_word(self):
        return choice(self.words)


    def make_guess(self):
        bad_guess = True
        while bad_guess:
            user_guess = input(f"Guess a {self.letters} letter word: ").lower()
            if len(user_guess) != self.letters:
                print(f"Words must be {self.letters} letters long, try again!")
                continue
            elif user_guess in self.guesses:
                print(f"You already guessed {user_guess}, try again!")
                continue
            else:
                bad_guess = False
                self.guess = user_guess
                self.guesses[self.tries] = self.guess
                self.tries += 1        

    
    def play_game(self):
        print(self.logo)
        print("Welcome to Wordle!")
        while self.tries < 6:
            self.make_guess()
            self.update_display()
            if self.guess == self.game_word:
                print(f"YOU WIN! {self.tries}/6 THE WORD WAS '{self.game_word.upper()}'! ")
                # implement play again here
                return

        print(f"Sorry you are out of tries, the word was {self.game_word}")


    def update_display(self):
        os.system("clear")
        for word in self.guesses:
            if len(word) > 0:
                display = []
                for index, letter in enumerate(word):
                    if letter == self.game_word[index]:
                        display.extend([Back.GREEN, letter.upper(), Style.RESET_ALL, ' '])
                    elif letter in self.game_word and letter != self.game_word[index]:
                         display.extend([Back.YELLOW, letter.upper(), Style.RESET_ALL, ' '])
                    else:
                         display.extend([Style.RESET_ALL, letter.upper(), Style.RESET_ALL, ' '])

                for index, word in enumerate(display):
                    if index == (len(display) -1):
                        print(word)
                    else:
                        print(word, end="")


            else:
                display = [ "_" for _ in range(len(self.game_word))]
                print(' '.join(display))


Wordle(6)