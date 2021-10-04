"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub
# , concat

__author__ = "730385108"


def test_only_evens() -> None: 
    x: list[int] = [2, 7]
    assert only_evens(x) == [2]


def test_only_evens1() -> None: 
    x: list[int] = [3, 4, 7]
    assert only_evens(x) == [4]


def test_only_evens2() -> None: 
    x: list[int] = [1, 5, 7]
    assert only_evens(x) == []


def test_sub1() -> None: 
    z: list[int] = [1]
    x: int 
    y: int 
    assert sub(z, x, y) == 1


def test_sub2() -> None: 
    z: list[int] = [1, 2, 3, 4, 5]
    x: 3
    y: 4
    assert sub(z, x, y) == [4, 5]


def test_sub3() -> None: 
    z: list[int] = [10, 20, 30, 40]
    x: int = 1
    y: int = 3
    assert sub(z, x, y) == [20, 40]