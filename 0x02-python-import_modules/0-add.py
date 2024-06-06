#!/usr/bin/python3
module_name = "0-add"
module = __import__(module_name)

a = 1
b = 2

result = module.add(a, b)

print("{} + {} = {}".format(a, b, result))
