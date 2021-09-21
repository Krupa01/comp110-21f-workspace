"""This is my project 00. The purpose of the 'Guess the Magical Number Game' is to ask the user to select range they would like to play from and then get the user to guess the magic number. The code will give the user hints and award points for the right answer. The user has 5 attempts to guess."""


__author__ = "730385108"

import random

SMILE: str = "\U0001f600"
SAD: str = u"\U0001F622"
UP: str = u"\u2B06\uFE0F"
DOWN: str = u"\u2B07\uFE0F"
YAY: str = "\U0001f389"

points: int = 0
player: str = ("name")


def greet() -> None:
    """This greets the player by first asking for thier name."""
    global player
    player = input("Hey, what's your name? ")
    print(f"Welcome to 'Guess the Magical Number Game' {player}!")


def main() -> None:
    """This asks users to choose the range for the game they want to play. Its a place to run my game."""
    greet()
    global points
    print(f"You will earn a point for each correct guess! {SMILE}")
    prompt: str = ""
    i = int(0)
    while i < 1000:
        prompt = str(input("Would you like to guess the magic number between a) 1-10, b) 1-50, or c) 1-100 ? Please type a , b, or c. If you would like to leave the game type 'quit'. "))
        print(prompt)
        if prompt == "a":
            game(10, 5)
        elif prompt == "b":
            game(50, 5)
        elif prompt == "c":
            game(100, 5)
        elif prompt == "quit": 
            quit_game()


def game(n: int, a: int) -> int:
    """This contains the code that will run the game. It will ask user for input and whether they got it right or wrong."""
    print(f"You choose to guess a number that is between 1 - {n}.")
    global points
    magic_number = random.randint(1, n)
    t: int = 0
    while t < a:
        guess = int(input("What's your guess?: "))
        if guess == magic_number:
            print(f"You got it! {SMILE}")
            points += 1
            return points
        else:
            if guess > magic_number:
                print(f"Guess lower {DOWN}")
            else:
                print(f"Guess Higher {UP}")
        t += 1
    print(f"Out of attempts, try playing again. {SAD}")
    print(f"So far you have {points} points. {YAY}")
    return(points)


def quit_game() -> None:
    """This will allow the user to quit the game."""
    print(f"Thanks for playing! You have earned {points} this game! {YAY}")
    quit()


if __name__ == "__main__":
    main()
