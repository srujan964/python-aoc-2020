#!/usr/bin/python3

with open('input.txt') as f:
    contents = f.read().splitlines()


def get_seat_id(seat):
    seat_id = seat.translate(str.maketrans('FBLR', '0101'))
    return int(seat_id, 2)


def get_my_seat():
    seat_ids = set(get_seat_id(seat) for seat in contents)
    return set(range(min(seat_ids), max(seat_ids))) - seat_ids


print(max(get_seat_id(seat) for seat in contents))

print(get_my_seat())
