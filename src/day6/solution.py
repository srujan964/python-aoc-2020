#!/usr/bin/python3

with open('input.txt') as f:
    contents = f.read().split('\n\n')

groups = [group.split('\n') for group in contents]


def part1():
    questions_per_group = list(map(set, [''.join(group) for group in groups]))
    return sum(map(len, questions_per_group))


def part2():
    questions_answered_by_all = [set.intersection(
        *[set(person) for person in group]) for group in groups]
    return sum(map(len, questions_answered_by_all))


print(part1())
print(part2())
