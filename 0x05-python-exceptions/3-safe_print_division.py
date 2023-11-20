#!/usr/bin/python3
def safe_print_division(a, b):
    quote = None
    try:
        quote = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(quote))
        return quote
