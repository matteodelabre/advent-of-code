scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
score = 0

try:
    while True:
        line = input()
        stack = []

        for c in line:
            if c in closing:
                stack.append(closing[c])
            else:
                if stack.pop() != c:
                    score += scores[c]
                    break
except EOFError:
    pass

print(score)
