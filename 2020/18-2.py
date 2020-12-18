tok_add = '+'
tok_mul = '*'
tok_parop = '('
tok_parcl = ')'
tok_num = 'number'

def tokenize(string):
    tokens = []
    i = 0

    while i < len(string):
        if string[i] == ' ':
            i += 1
            continue
        elif string[i] == '+':
            tokens.append((tok_add,))
            i += 1
        elif string[i] == '*':
            tokens.append((tok_mul,))
            i += 1
        elif string[i] == '(':
            tokens.append((tok_parop,))
            i += 1
        elif string[i] == ')':
            tokens.append((tok_parcl,))
            i += 1
        elif string[i].isdigit():
            j = i

            while j < len(string) and string[j].isdigit():
                j += 1

            tokens.append((tok_num, int(string[i:j])))
            i = j
        else:
            raise ValueError(f'Unknown character {string[i]}')

    return tokens

def parse(tokens):
    next_mul = 0
    count = 0

    while next_mul < len(tokens) and (count > 0 or tokens[next_mul][0] != tok_mul):
        if tokens[next_mul][0] == tok_parop:
            count += 1
        elif tokens[next_mul][0] == tok_parcl:
            count -= 1

        next_mul += 1

    if next_mul < len(tokens):
        return parse(tokens[0:next_mul]) * parse(tokens[next_mul + 1:])

    if tokens[0][0] == tok_parop:
        par_end = 1
        count = 1

        while par_end < len(tokens) and count > 0:
            if tokens[par_end][0] == tok_parop:
                count += 1
            elif tokens[par_end][0] == tok_parcl:
                count -= 1

            par_end += 1

        assert count == 0

        if par_end == len(tokens):
            return parse(tokens[1:-1])
        else:
            return parse(tokens[1:par_end - 1]) + parse(tokens[par_end + 1:])

    if len(tokens) == 1:
        return tokens[0][1]
    else:
        return tokens[0][1] + parse(tokens[2:])

total = 0

try:
    while True:
        total += parse(tokenize(input()))
except EOFError:
    pass

print(total)
