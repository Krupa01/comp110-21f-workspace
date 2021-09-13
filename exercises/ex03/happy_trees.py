"""Drawing forests in a loop."""

__author__ = "1730385108"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
number: int = int(input("Depth: "))
i: int = 1
while i <= number: 
    print(TREE * i)
    i += 1