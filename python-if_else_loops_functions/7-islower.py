#!/bin/
def islower(c):
    # Check if the ASCII value of 'c' is in the range of lowercase letters (97-122)
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
# Testing the function
if __name__ == "__main__":
    is_lower = __import__('7-islower').islower
    print("a is {}".format("lower" if is_lower("a") else "upper"))
    print("H is {}".format("lower" if is_lower("H") else "upper"))
    print("A is {}".format("lower" if is_lower("A") else "upper"))
    print("3 is {}".format("lower" if is_lower("3") else "upper"))
    print("g is {}".format("lower" if is_lower("g") else "upper"))
