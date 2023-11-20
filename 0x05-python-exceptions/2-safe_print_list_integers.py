#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numm = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            numm += 1
        except (TypeError, ValueError):
            pass
    print()
    return numm
