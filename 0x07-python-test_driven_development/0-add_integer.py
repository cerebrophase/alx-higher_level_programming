#!/usr/bin/python3
def add_integer(a, b=98):
    """ adds two integers a and b """


    if not isinstance (a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance (b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    a = int(b)

    return a + b


