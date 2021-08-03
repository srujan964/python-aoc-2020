#!/usr/bin/python3

with open('input.txt') as f:
    contents = [line.strip() for line in f.readlines()]


def p1_is_valid(line):
    policy_range, ch, pwd = line.split(' ')
    l, h = list(map(int, policy_range.split('-')))
    return l <= pwd.count(ch[0]) <= h


def p2_is_valid(line):
    policy_range, ch, pwd = line.split(' ')
    i1, i2 = list(map(int, policy_range.split('-')))
    return (pwd[i1 - 1] == ch[0]) ^ (pwd[i2 - 1] == ch[0])


p1_valid_pwds = list(filter(p1_is_valid, contents))
print(len(p1_valid_pwds))

p2_valid_pwds = list(filter(p2_is_valid, contents))
print(len(p2_valid_pwds))
