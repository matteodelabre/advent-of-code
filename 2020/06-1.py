current_answers = set()
total = 0

try:
    while True:
        line = input().strip()

        if not line:
            total += len(current_answers)
            current_answers = set()
        else:
            current_answers.update(line)
except EOFError:
    pass

total += len(current_answers)
print(total)
