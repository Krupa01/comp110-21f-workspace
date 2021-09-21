"""DOcStRING...."""


__author__ = "730385108"

import random

SMILE: str = "\U0001f600"
SAD: str = u"\U0001F622"
UP: str = u"\u2B06\uFE0F"
DOWN: str = u"\u2B07\uFE0F"
YAY: str = u"\U000FE517"

points: int = 0
player: str = ("name")


def greet() -> None:
    """blah."""
    global player
    player = input("Hey, what's your name? ")
    print(f"Welcome to 'Guess the Magical Number Game' {player}!")


def main() -> None:
    """DOCstring."""
    greet()
    global points
    print("You will earn a point for each correct guess!")
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
    """This is the start_game..."""
    print(f"You choose to guess a number that is between 1 - {n}.")
    global points
    magic_number = random.randint(1, n)
    t: int = 0
    while t < a:
        guess = int(input("What's your guess?: "))
        if guess == magic_number:
            print("You got it...")
            points += 1
            return points
        else:
            if guess > magic_number:
                print("Too high")
            else:
                print("too low")
        t += 1
    print("Out of attempts, try playing again.")
    print(f"So far you have {points} points.")
    return(points)


def quit_game() -> None:
    """Quit."""
    print(f"Thanks for playing! You have earned {points} this game! {YAY}")
    quit()


if __name__ == "__main__":
    main()
