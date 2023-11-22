#!/usr/bin/python3
def magic_string(): magic_string.count = getattr(magic_string, 'count', 0) + 1;
    return "Holberton" * magic_string.count
print(magic_string(), magic_string(), magic_string(), end=" ");[print(magic_string()) for _ in range(30)]
