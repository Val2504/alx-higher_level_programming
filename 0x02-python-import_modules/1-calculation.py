#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

for_add = add(a, b)
for_sub = sub(a, b)
for_mul = mul(a, b)
for_div = int(div(a, b))

if __name__ =="__main__"
print("{} + {} = {}".format(a, b, for_add))
print("{} - {} = {}".format(a, b, for_sub))
print("{} * {} = {}".format(a, b, for_mul))
print("{} / {} = {}".format(a, b, for_div))
