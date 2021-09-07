"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730385108"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
# from random import randint

import random
Message = random.randint(1, 4) 
print("Your fortune cookie says...")

Message_1 = "Everything happens for a reason."
Message_2 = "You will reach your goals soon."
Message_3 = "You are a smart and beautiful person."
Message_4 = "Believe in yourself!"

if Message == 1:
    print(Message_1)
else: 
    ("No Fortune")
if Message == 2:
    print(Message_2)
else: 
    ("No Fortune")
if Message == 3:
    print(Message_3)
else: 
    ("No Fortune")    
if Message == 4:
    print(Message_4)
else:
    ("No Fortune") 
print("Now, go spread positive vibes!")
