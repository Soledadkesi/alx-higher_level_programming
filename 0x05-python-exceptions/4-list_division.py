#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newListt = []
    for i in range(list_length):
        divv = 0
        try:
            divv = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            newListt.append(divv)
    return newListt
