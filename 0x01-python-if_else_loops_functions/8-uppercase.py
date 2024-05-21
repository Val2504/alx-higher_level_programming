#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if not ('A' <= char <= 'Z'):
            raise ValueError('it is not an uppercase')
        print("{}".format(char), end='')
    print()
