#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
    except (IndexError, ValueError, TypeError):
        pass
    return count
if __name__ == "__main__":
    # Example usage:
    my_list = [1, "not_an_integer", 2, 3, "another_string"]
    nb_integers = safe_print_list_integers(my_list, 4)
    print("Number of integers printed: {:d}".format(nb_integers))
