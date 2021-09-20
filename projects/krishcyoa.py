"""DOcStRING...."""


__author__ = "730385108"

import random

SMILE: str = "\U0001f600"
SAD: str = u"\U0001F622"
UP: str = u"\u2B06\uFE0F"
DOWN: str = u"\u2B07\uFE0F"
YAY: str = u"\U000FE517"

points: int = 1
player: str = ("name")
attempts: int = 1


def greet() -> None:
    """blah."""
    global player
    player = input("Hey, what's your name? ")
    print(f"Welcome to 'Guess the Magical Number Game' {player}!")


def main() -> None:
    """DOCstring."""
    greet()
    global points
    print("You have 5 attempts to guess the correct number. You will earn a point for each correct quess!")
    points += 1
    i = int(0)
    global attempts 
    attempts += 1
    i = int(0)
    while i < 1000:
        prompt: str = input("Would you like to guess the magic number between a) 1-10, b) 1-50, or c) 1-100 ? Please type a , b, or c. If you would like to leave the game type 'quit'. ")
        if prompt == "a" or "A":
            game(10)
        elif prompt == "b" or "B":
            game(50)
        elif prompt == "c" or "C":
            game(100)
        elif prompt == "quit" or "Quit": 
            quit_game()
        else:
            print("Invalid Output")
    if points == 1:
        print(f"Sorry {player} you lost! You had {points} attempts {SAD}")
    else:
        print(f"You won with {points} attempts!!! {SMILE}")


def game(n: int) -> int:
    """This is the start_game..."""
    global points
    points += 1 
    guess = int(input("What's your guess?: "))
    magic_number = random.randint(1, n)
    global attempts
    attempts += 1
    while guess != magic_number and attempts > 5:
        if magic_number < guess:
            print(f"Guess lower {DOWN}")
            points += 1
        elif magic_number > guess:
            print(f"Guess higher {UP}") 
            points += 1
        guess = int(input("What's your guess?: "))
        if attempts >= 5:
            print(f"Sorry you lost! You ran out of attempts. {SAD} You have {points} points.")
        elif magic_number == guess:
            print("You guessed it! The number was", magic_number)
            print(f"You won with {points} attempts!!! {SMILE}.")
    return(points)


def quit_game() -> None:
    print(f"Thanks for playing! You have earned {points} this game! {YAY}")
    quit()


if __name__ == "__main__":
    main()
