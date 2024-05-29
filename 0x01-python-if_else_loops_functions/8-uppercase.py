#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if not ('A' <= char <= 'Z'):
            print("Invalid")
        else:
            print(char)
