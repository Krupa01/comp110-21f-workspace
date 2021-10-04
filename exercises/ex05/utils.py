"""List utility functions part 2."""

__author__ = "730385108"


def only_evens(x: list[int]) -> list[int]:
    """This function will print the even numbers in the list."""
    i: int = 0
    evens = list()
    while (i < len(x)):
        if x[i] % 2 == 0: 
            evens.append(x[i])
            i += 1
        else:
            i += 1
    return evens


def sub(z: list[int], x: int, y: int) -> list[int]: 
    """This function creates a subset."""
    i: int = 0
    lists = list()
    end: int = y
    start: int = x
    if len(z) == 0 or end <= 0 or len(z) < start:
        return lists
    elif len(z) < end: 
        while len(z) > start:
            lists.append(z[start])
            start += 1 
        return lists
    elif start >= 0: 
        while end > start: 
            lists.append(z[start])
            start += 1 
        return lists
    elif start < 0: 
        while end > i:
            lists.append(z[i])
            i += 1
        return lists
    return z


def concat(x: list[int], y: list[int]) -> list[int]:
    """This function concats two lists."""
    con = list()
    i: int = 0
    count: int = 0
    while len(y) > i: 
        con.append(y[i])
        i += 1
    while len(x) > count: 
        con.append(x[count])
        count += 1 
    return con