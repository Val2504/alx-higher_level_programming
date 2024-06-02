#!/usr/bin/python3
def add(a, b):
    if a > 0 and b > 0:
        result = a + b
    elif a < 0 and b > 0:
        result = -a + b
    elif a > 0 and b < 0:
        result = a + (-b)
    elif a < 0 and b < 0:
        result = (-a) + (-b)

    return result
