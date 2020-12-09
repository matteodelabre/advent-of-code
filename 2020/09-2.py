import sys

target = 23278925

numbers = [0]
last_sum = 0
summed_numbers = [0]

try:
    while True:
        numbers.append(int(input()))
        last_sum += numbers[-1]
        summed_numbers.append(last_sum)
except EOFError:
    pass

for i in range(1, len(summed_numbers)):
    for j in range(i + 1, len(summed_numbers)):
        if summed_numbers[j] - summed_numbers[i - 1] == target:
            print(min(numbers[i:j+1]) + max(numbers[i:j+1]))
            sys.exit()

print('not found')
