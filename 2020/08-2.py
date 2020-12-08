import re

instruction_regex = re.compile(r'(nop|acc|jmp) ([+-][0-9]+)')
program = []

try:
    while True:
        name, arg = instruction_regex.match(input()).groups()
        program.append([name, arg])
except EOFError:
    pass

for change in range(len(program)):
    if program[change][0] == 'nop':
        program[change][0] = 'jmp'
    elif program[change][0] == 'jmp':
        program[change][0] = 'nop'
    else:
        continue

    pc = 0
    executed = set()
    accu = 0

    while pc not in executed and pc < len(program):
        executed.add(pc)

        if program[pc][0] == 'nop':
            pc += 1
        elif program[pc][0] == 'acc':
            accu += int(program[pc][1])
            pc += 1
        elif program[pc][0] == 'jmp':
            pc += int(program[pc][1])
        else:
            print('invalid instruction:', program[pc][0])

    if pc == len(program):
        break
    else:
        accu = -1

    if program[change][0] == 'nop':
        program[change][0] = 'jmp'
    elif program[change][0] == 'jmp':
        program[change][0] = 'nop'

print(accu)
