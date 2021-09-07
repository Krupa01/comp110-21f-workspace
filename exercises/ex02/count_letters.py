"""Counting letters in a string."""

__author__ = "730385108"


letter = input("What letter do you want to seach for?: ")
word = input("Enter a word: ")
counter = 0
i = 0

while len(word) > i:
    if(word[i] == letter):
        counter = counter + 1
    i = i + 1
print("Count:", counter)