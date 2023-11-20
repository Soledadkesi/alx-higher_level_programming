#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    num_printed = 0
    index = 0
    while num_printed < x:
        try:
            print("{}".format(my_list[index]), end="")
            num_printed += 1
        except IndexError:
            break
        index += 1
    print()
    return num_printed
