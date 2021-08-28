"""This is EX01 input and variables: Hype Machine. In this exercise I had to write a code in which a user can input thier name and would receive responses that would contain thier name in the beginning, middle, and end of a sentence."""

__author__ = ("730385108")

name: str = input("What is your name? ")
print("You entered: ")
print(name)

print(name + ", you look amazing today!")
print("I hope your day is going well " + name + "!")
print("I believe you, " + name + ", will do great things today!")