"""Counting letters in a string."""

__author__ = "730385108"


letter = input("What letter do you want to seach for?: ")
word = input("Enter a word: ")
count = 0
i = 0

while i < len(word):
    if(word[i] == letter):
        count = count + 1
    i = i + 1

print("Count:", count)