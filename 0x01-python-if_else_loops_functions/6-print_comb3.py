#!/usr/bin/python3
for val in range(0, 10):
    for num in range(val + 1, 10):
        print("{}{}".format(val, num), end=' ')
        if val != 9 and num != val - 1:
