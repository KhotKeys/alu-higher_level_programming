#!/usr/bin/python3
def magic_string(): magic_string.count = getattr(magic_string, 'count', 0) + 1; return "Holberton" * magic_string.count
print(magic_string())
print(magic_string()); print(magic_string())
for i in range(30): print(magic_string())
