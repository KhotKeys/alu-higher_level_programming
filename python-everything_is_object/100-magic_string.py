#!/usr/bin/python3

def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "Holberton" * magic_string.count

# Test case for main_0.py
print(magic_string())

# Test case for main_1.py
for i in range(30):
    print(magic_string())

# Test case for main_2.py
for i in range(13):
    count, result = magic_string()
    print(count)
    print(result)
