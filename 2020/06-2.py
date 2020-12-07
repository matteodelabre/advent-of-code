from string import ascii_lowercase as alphabet

current_answers = set(alphabet)
total = 0

try:
    while True:
        line = input().strip()

        if not line:
            total += len(current_answers)
            current_answers = set(alphabet)
        else:
            current_answers &= set(line)
except EOFError:
    pass

total += len(current_answers)
print(total)
