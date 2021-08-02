#!/usr/bin/python3
from itertools import combinations

with open('input.txt') as f:
    data = list(map(int, f.readlines()))

x = next(filter(lambda x: x[0] + x[1] == 2020, combinations(data, 2)), None)
y = next(filter(lambda x: x[0] + x[1] + x[2]
         == 2020, combinations(data, 3)), None)

print(x[0] * x[1])
print(y[0] * y[1] * y[2])
