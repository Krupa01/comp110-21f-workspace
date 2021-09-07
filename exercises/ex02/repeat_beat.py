"""Repeating a beat in a loop."""

__author__ = "730385108"


beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
counter: int = 0
if counter < repeat:
    print(((beat + " ") * (repeat - 1)) + beat)
else: 
    if repeat <= 0:
        print("No beat...")