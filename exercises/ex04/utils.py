"""List utility functions."""

__author__ = "730385108"


def all(x: list[int], y: int, ) -> bool:
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
    it: int = 0 
    ji: bool = False 
    if len(x) == 0 and len(y) == 0:
        return True
    while it < len(x) and it < len(y):
        if len(x) == len(y):
            if x[it] == y[it]:
                ji = True
                it += 1
            else:
                ji = False
                return False
        else: 
            return False 
    return ji 


def max(input: list[int]) -> int:
    """The last functions find the max in the list.""" 
    if len(input) == 0:
        raise ValueError("max() arg is an empty List") 
    else:
        maxim = input[0]
        for number in input:
            if number > maxim:
                maxim = number
    return maxim 