"""Finding duplicate letters in a word."""

__author__ = "730385108"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0

while len(word) > i:
    j: int = i + 1
    while j < len(word):
        if(word[i] == word[j]):
            dup = True 
        j += 1
    i += 1
print("Found duplicate:", dup)
