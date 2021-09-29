"""List utility functions."""

__author__ = "730385108"


def all(x: int, y: list[int]) -> bool:
    """This is the first function that returns a bool."""
    j: bool = False
    i: int = 0
    while i < len(y):
        if y[i] == x:
            j = True
            i += 1
        else:
            j = False
            return j
    return j


def is_equal(x: list[int], y: list[int]) -> int:
    """Function two returns True if both lists are the same."""
    i: int = 0 
    count: int = 0
    j: bool = False 
    while len(x) == len(y):
        if x[i] == y[i]:
            count += 1
        if count == len(x): 
            j = True
        i += 1
    return j 


def max(input: list[int]) -> int:
    """The last functions find the max in the list.""" 
    if len(input) == 0:
        raise ValueError("max() arg is an empty List") 
    for x in range(0, len(input)): 
        if(input[i] > i): 
            input[i] = i
    return i 

