"""This is EX01 input and variables: Relational_operators. In this exercise I wrote a code that when users entered two numbers it would calculate relational operations and determine weather the statement is True or False (Boolean)."""

__author__ = ("730385108")

variable_one: int = int(input("Left-hand side: "))

variable_two: int = int(input("Right-hand side: "))

print(variable_one, "<", variable_two, "is", variable_one < variable_two)
print(variable_one, ">=", variable_two, "is", variable_one >= variable_two)
print(variable_one, "==", variable_two, "is", variable_one == variable_two) 
print(variable_one, "!=", variable_two, "is", variable_one != variable_two) 