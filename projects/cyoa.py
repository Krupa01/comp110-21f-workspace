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


def greet() -> None:
    """blah."""
    global player
    player = input("Hey, what's your name? ")
    print(f"Welcome to 'Guess the Magical Number Game' {player}!")


def main() -> None:
    """DOCstring."""
    greet()
    global points
    print("You have 5 attempts to guess the correct number. The less points the better!")
    i = int(0)
    while i < 1000:
        prompt: str = input("Would you like to guess the magic number between a) 1-10, b) 1-50, or c) 1-100 ? Please type a , b, or c. \n "
                            "If you would like to leave the game type 'quit'.")
        if prompt == "a" or "A":
            game_a(10)
        elif prompt == "b" or "B":
            game_b(50)
        elif prompt == "c" or "C":
            game_c(100)
        elif prompt == "quit" or "Quit": 
            quit_game()
        i += 1
    if points > 5:
        print(f"Sorry {player} you lost! You had {points} attempts {SAD}")
    else:
        print(f"You won with {points} attempts!!! {SMILE}")


def game_a(n: int) -> int:
    """This is the start_game..."""
    global points 
    guess = int(input("What's your guess?: "))
    magic_number = random.randint(1, 10)
    attempts = 5
    while guess != magic_number and attempts > points:
        if magic_number < guess:
            print(f"Guess lower {DOWN}")
            points += 1
        elif magic_number > guess:
            print(f"Guess higher {UP}") 
            points += 1
        guess = int(input("What's your guess?: "))
    if points >= attempts:
        print(f"Sorry you lost! You ran out of attempts {SAD}")
    elif magic_number == guess:
        print("You guessed it! The number was", magic_number)
        print(f"You won with {points} attempts!!! {SMILE}")
    return(points)


def game_b(n: int) -> int:
    """This is the start_game..."""
    global points 
    guess = int(input("What's your guess?: "))
    magic_number = random.randint(1, 50)
    attempts = 5
    while guess != magic_number and attempts > points:
        if magic_number < guess:
            print(f"Guess lower {DOWN}")
            points += 1
        elif magic_number > guess:
            print(f"Guess higher {UP}") 
            points += 1
        guess = int(input("What's your guess?: "))
    if points >= attempts:
        print(f"Sorry you lost! You ran out of attempts {SAD}")
    elif magic_number == guess:
        print("You guessed it! The number was", magic_number)
        print(f"You won with {points} attempts!!! {SMILE}")
    return(points)


def game_c(n: int) -> int:
    """This is the start_game..."""
    global points
    guess = int(input("What's your guess?: "))
    magic_number = random.randint(1, 100)
    attempts = 5
    while guess != magic_number and attempts > points:
        if magic_number < guess:
            print(f"Guess lower {DOWN}")
            points += 1
        elif magic_number > guess:
            print(f"Guess higher {UP}") 
            points += 1
        guess = int(input("What's your guess?: "))
    if points >= attempts:
        print(f"Sorry you lost! You ran out of attempts {SAD}")
    elif magic_number == guess:
        print("You guessed it! The number was", magic_number)
        print(f"You won with {points} attempts!!! {SMILE}")
    return(points)


def quit_game() -> None:
    print(f"Thanks for playing! You have earned {points} this game! {YAY}")
    quit()


if __name__ == "__main__":
    main()