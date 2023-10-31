#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        a = i % 5 == 0
        s = i % 3 == 0
        k = a and s
        str = f"FizzBuzz" if k else f"Buzz" if a \
            else f"Fizz" if s else f"{i:d}"
        print(str, end=" ")
