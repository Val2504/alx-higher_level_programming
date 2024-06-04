#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

for_add = add(a, b)
print("{} + {} = {}".format(a, b, for_add))

for_sub = sub(a, b)
print("{} - {} = {}".format(a, b, for_sub))

for_mul = mul(a, b)
print("{} * {} = {}".format(a, b, for_mul))

for_div = int(div(a, b))
print("{} / {} = {}".format(a, b, for_div))
