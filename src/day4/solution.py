#!/usr/bin/python3

import re

with open('input.txt') as f:
    contents = f.read().split('\n\n')


def has_all_fields(passport):
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport for field in valid_fields)


def is_valid(passport):
    if not has_all_fields(passport):
        return False

    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            return False
    else:
        return False

    if not re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$').match(passport['hcl']):
        return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not re.compile(r'^(\d{9})$').match(passport['pid']):
        return False

    return True


passports = [line.strip().replace(' ', '\n').split('\n') for line in contents]
passports = [dict(v.split(':') for v in passport) for passport in passports]

print(sum(has_all_fields(passport) for passport in passports))
print(sum(is_valid(passport) for passport in passports))
