"""This is EX01 input and variables: Numeric Operators. In thier exercise I had to write a code that would ask a user to input two variables for the left hand side and the right hand side. It would then have to perform numerical operations."""

__author__ = ("730385108")

variable_one: int = int(input("Left-hand side: "))

variable_two: int = int(input("Right-hand side: "))

print(variable_one, "**", variable_two, "is", variable_one ** variable_two)
print(variable_one, "/", variable_two, "is", variable_one / variable_two)
print(variable_one, "//", variable_two, "is", variable_one // variable_two) 
print(variable_one, "%", variable_two, "is", variable_one % variable_two) 
