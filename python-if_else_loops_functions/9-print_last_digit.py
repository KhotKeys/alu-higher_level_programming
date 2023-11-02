#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit by taking the absolute value of the number and then using modulo 10
    last_digit = abs(number) % 10
    print(last_digit, end='')

# Testing the function
if __name__ == "__main__":
    print_last_digit = __import__('9-print_last_digit').print_last_digit

    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
