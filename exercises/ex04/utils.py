"""List utility functions."""

__author__ = "730385108"


def all(x: list[int], y: int) -> bool:
    """This is the first function that returns a bool."""
    j: bool = False
    i: int = 0
    while i < len(x):
        if x[i] == y:
            j = True
            i += 1
        else:
            j = False
            return j
    return j


def is_equal(x: list[int], y: list[int]) -> bool:
    """Function two returns True if both lists are the same."""
    i: int = 0 
    j: bool = False 
    if len(x) = 0 
    while i < len(x) and i < len(y):
        if len(x) == len(y):
            if x[i] == y[i]:
                j = True
                i += 1
            else:
                j = False
                return False
    return j 


def max(input: list[int]) -> int:
    """The last functions find the max in the list.""" 
    if len(input) == 0:
        raise ValueError("max() arg is an empty List") 
    for x in range(0, len(input)): 
        if(input[i] > i): 
            input[i] = i
    return i 

