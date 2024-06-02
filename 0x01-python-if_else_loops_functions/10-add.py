#!/usr/bin/python3
def add(a, b):
    if a > 0 and b > 0:
        return (a + b)
    elif a < 0 and b > 0:
        return (-a + b)
    elif a > 0 and b < 0:
        return (a + (-b))
    else if a < 0 and b < 0:
        return ((-a) + (-b))
