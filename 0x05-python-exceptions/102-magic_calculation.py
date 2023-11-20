#!/usr/bin/python3
def magic_calculation(a, b):
    resultt = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                resultt += (a**b)/j
        except Exception:
            resultt = b + a
            break
    return resultt
