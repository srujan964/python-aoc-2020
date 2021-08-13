#!/usr/bin/python3
from pprint import pprint

with open('input.txt') as f:
    data = f.read().splitlines()

accumulator = 0
program_counter = 0
processed = set()


def jump(pc, acc, arg):
    pc += arg
    return pc, acc


def accumulate(pc, acc, arg):
    acc += arg
    pc += 1
    return pc, acc


def no_op(pc, acc, arg):
    pc += 1
    return pc, acc


instr_table = {
    'jmp': jump,
    'acc': accumulate,
    'nop': no_op
}


def execute(instr, arg, pc, acc):
    return instr_table[instr](pc, acc, arg)


while True:
    if program_counter in processed:
        print(accumulator)
        break
    processed.add(program_counter)
    instr, arg = data[program_counter].split()
    arg = int(arg)

    program_counter, accumulator = execute(
        instr, arg, program_counter, accumulator)


def fix_prog(prog):
    accumulator = 0
    program_counter = 0
    processed = set()

    while True:
        if program_counter == len(prog):
            return accumulator
        if program_counter in processed:
            return None
        processed.add(program_counter)

        line = prog[program_counter]

        instr, arg = line.split()
        arg = int(arg)

        program_counter, accumulator = execute(
            instr, arg, program_counter, accumulator)


for i in range(len(data)):
    prog = list(data)
    if prog[i].startswith('jmp'):
        prog[i] = prog[i].replace('jmp', 'nop')
    elif prog[i].startswith('nop'):
        prog[i] = prog[i].replace('nop', 'jmp')
    x = fix_prog(prog)
    if x:
        print(x)
