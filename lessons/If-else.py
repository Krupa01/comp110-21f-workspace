"""Challenge Question #1."""

# Print A if choice < 25
# Print B if choice is >= 25 AND < 50
# Print C if choice > 75
# Print D if choice >= 50 and <= 75

choice: int = int(input("Enter a number:"))
if choice < 25:
    print("A")
else: 
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")