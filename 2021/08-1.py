result = 0

try:
    while True:
        _, outputs = input().split(" | ")
        result += sum(len(output) in (2, 3, 4, 7) for output in outputs.split())
except EOFError:
    pass

print(result)
