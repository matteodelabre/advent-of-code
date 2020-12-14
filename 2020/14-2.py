from collections import defaultdict
import re

raw_mask = '0' * 36
total_float = 0
mask_fixed = 0
mask_over = 0

memory = defaultdict(int)
instr_regex = re.compile(r'mem\[(\d+)\] = (\d+)')

try:
    while True:
        line = input()

        if line[:4] == 'mask':
            raw_mask = line[7:]
            total_float = 0
            mask_fixed = 0
            mask_over = 0

            for i in range(36):
                if raw_mask[35 - i] == 'X':
                    total_float += 1
                else:
                    mask_fixed |= (1 << i)

                    if raw_mask[35 - i] == '1':
                        mask_over |= (1 << i)

        else:
            addr, val = instr_regex.match(line).groups()
            addr = (int(addr) | mask_over) & mask_fixed

            for i in range(1 << total_float):
                repl = bin(i)[2:]
                repl = '0' * (total_float - len(repl)) + repl

                next_bit = total_float - 1
                mask_value = 0

                for j in range(36):
                    if raw_mask[35 - j] == 'X':
                        if repl[next_bit] == '1':
                            mask_value |= (1 << j)

                        next_bit -= 1

                memory[addr | mask_value] = int(val)
except EOFError:
    pass

print(sum(memory.values()))
