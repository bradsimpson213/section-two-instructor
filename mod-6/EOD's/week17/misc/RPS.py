import random


def show_pic(item):
    ascii_art = {
        "rock": """
TBD--ROCK
""",
        "paper": """
TBD--PAPER
""",
        "scissors": """
TBD--SCISSORS
""",
        "lizard": """
TBD--LIZARD
""",
        "spock": """
TBD--SPOCK
"""
    }
    print(ascii_art.get(item, "404: picture not found"))

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

def get_user_choice():
    print(f"Enter choice: {', '.join(VALID_CHOICES)}")
    user_choice = input("Your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def determine_winner(user_choice, computer_choice):
    outcomes = {
        ("paper", "rock"): "Paper covers rock. You win!",
        ("rock", "scissors"): "Rock crushes scissors. You win!",
        ("scissors", "paper"): "Scissors cuts paper. You win!",
        ("rock", "lizard"): "Rock crushes lizard. You win!",
        ("lizard", "spock"): "Lizard poisons Spock. You win!",
        ("spock", "scissors"): "Spock smashes scissors. You win!",
        ("scissors", "lizard"): "Scissors decapitates lizard. You win!",
        ("lizard", "paper"): "Lizard eats paper. You win!",
        ("paper", "spock"): "Paper disproves Spock. You win!",
        ("spock", "rock"): "Spock vaporizes rock. You win!",
        ("rock", "paper"): "Paper covers rock. You lose.",
        ("scissors", "rock"): "Rock crushes scissors. You lose.",
        ("paper", "scissors"): "Scissors cuts paper. You lose.",
        ("lizard", "rock"): "Rock crushes lizard. You lose.",
        ("spock", "lizard"): "Lizard poisons Spock. You lose.",
        ("scissors", "spock"): "Spock smashes scissors. You lose.",
        ("lizard", "scissors"): "Scissors decapitates lizard. You lose.",
        ("paper", "lizard"): "Lizard eats paper. You lose.",
        ("spock", "paper"): "Paper disproves Spock. You lose.",
        ("rock", "spock"): "Spock vaporizes rock. You lose.",
    }
    result = outcomes.get((user_choice, computer_choice), "It's a tie!")
    return result

def start_game():
    print('''
    Welcome to the Rock, Paper, Scissors, Lizard, Spock game!
    A not-so-ancient battle where destiny is forged in the hands of the players!
    May the odds be ever in your favor!
          ''')
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}")
        if user_choice in VALID_CHOICES:
            show_pic(user_choice)
        else:
            print("Please make a valid selection")
            continue
        print(f"\Opponent chose {computer_choice}")
        show_pic(computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            exit()
            
start_game()

print("found end of file")