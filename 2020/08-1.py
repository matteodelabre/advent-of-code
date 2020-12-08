import re

instruction_regex = re.compile(r'(nop|acc|jmp) ([+-][0-9]+)')
program = []

try:
    while True:
        name, arg = instruction_regex.match(input()).groups()
        program.append([name, arg, 0])
except EOFError:
    pass

pc = 0
accu = 0

while program[pc][2] == 0:
    program[pc][2] = 1

    if program[pc][0] == 'nop':
        pc += 1
    elif program[pc][0] == 'acc':
        accu += int(program[pc][1])
        pc += 1
    elif program[pc][0] == 'jmp':
        pc += int(program[pc][1])
    else:
        print('invalid instruction:', program[pc][0])

print(accu)
