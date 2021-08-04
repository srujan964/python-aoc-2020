#!/usr/bin/python3
from functools import reduce

with open('input.txt') as f:
    contents = f.read().splitlines()


G = [[x == '#' for x in line] for line in contents]


def count_trees(right, down):
    ans = 0
    row = 0
    while (row * down) < len(G):
        if G[row * down][(row * right) % len(G[row * down])]:
            ans += 1
        row += 1
    return ans


print(count_trees(3, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
part2 = reduce(lambda a, b: a * b, [count_trees(*slope) for slope in slopes])
print(part2)
