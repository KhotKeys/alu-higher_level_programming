#!/usr/bin/python3
""" This function 'add_integer' takes in two arguments """
"""and returns the sum of the two."""


def add_integer(a, b=98):
    """Should the conditions be met, Raising the type error message"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
