#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer0
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
formatted_code = """#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)"""
print("Python script with str.format:")
print(formatted_code.format(code=formatted_code))
