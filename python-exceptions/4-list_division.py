#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Attempt the division
            division_result = 0

            if (isinstance(my_list_1[i], (int, float)) and
                    isinstance(my_list_2[i], (int, float)) and
                    my_list_2[i] != 0):
                division_result = my_list_1[i] / my_list_2[i]

            result.append(division_result)
        except (ZeroDivisionError, TypeError):
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            if division_result == 0 and isinstance(division_result, (int, float)):
                pass
            elif division_result == 0:
                print("division by 0")
            else:
                pass

    return result

if __name__ == "__main__":
    # Example usage:
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2))
    print(result)
    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2))
    print(result)
