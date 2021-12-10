scores = {")": 1, "]": 2, "}": 3, ">": 4}
closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
line_scores = []

try:
    while True:
        line = input()
        stack = []

        for c in line:
            if c in closing:
                stack.append(closing[c])
            else:
                if stack.pop() != c: break
        else:
            line_score = 0
            while stack:
                line_score *= 5
                line_score += scores[stack.pop()]
            line_scores.append(line_score)
except EOFError:
    pass

from statistics import median
print(median(line_scores))
