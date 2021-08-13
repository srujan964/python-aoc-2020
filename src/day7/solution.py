#!/usr/bin/python3

from collections import defaultdict
import re

with open('input.txt') as f:
    data = f.read().splitlines()


holdings = defaultdict(list)
contains = defaultdict(list)

for line in data:
    bag = re.match(r'\w+ \w+', line)[0]
    contents = re.findall(r'(\d+) (\w+ \w+)', line)
    for n, child in contents:
        holdings[child].append(bag)
        contains[bag].append((int(n), child))

contains_gold = set()


def has_gold(bag):
    for colour in holdings[bag]:
        contains_gold.add(colour)
        has_gold(colour)


has_gold('shiny gold')
print(len(contains_gold))


def count_required(bag):
    cnt = 0
    for n, child in contains[bag]:
        cnt += n * (1 + count_required(child))
    return cnt


print(count_required('shiny gold'))
