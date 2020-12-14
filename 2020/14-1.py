from collections import defaultdict
import re

keep_bits = (1 << 37) - 1
mask_value = 0

memory = defaultdict(int)
instr_regex = re.compile(r'mem\[(\d+)\] = (\d+)')

try:
    while True:
        line = input()

        if line[:4] == 'mask':
            raw_mask = line[7:]
            keep_bits = 0
            mask_value = 0

            for i in range(36):
                if raw_mask[35 - i] == 'X':
                    keep_bits |= (1 << i)
                elif raw_mask[35 - i] == '1':
                    mask_value |= (1 << i)

        else:
            addr, val = instr_regex.match(line).groups()
            val = (int(val) & keep_bits) | mask_value
            memory[addr] = val
            memory[addr] = int(val)
except EOFError:
    pass

print(sum(memory.values()))
