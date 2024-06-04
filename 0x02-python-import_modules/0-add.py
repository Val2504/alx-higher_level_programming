#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

def fake_add(a, b):
    return a - b

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, fake_add(a, b)))
