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

def parse(tokens, start):
    if tokens[start][0] == tok_parop:
        result, i = parse(tokens, start + 1)
    else:
        assert tokens[start][0] == tok_num
        result = tokens[start][1]
        i = start + 1

    while i < len(tokens):
        oper = tokens[i][0]

        if oper == tok_parcl:
            return (result, i + 1)

        if tokens[i + 1][0] == tok_num:
            right = tokens[i + 1][1]
            i += 2
        else:
            assert tokens[i + 1][0] == tok_parop
            right, i = parse(tokens, i + 2)

        if oper == tok_add:
            result += right
        elif oper == tok_mul:
            result *= right
        else:
            raise ValueError(f'Unexpected token {oper}')

    return (result, i)

total = 0

try:
    while True:
        total += parse(tokenize(input()), 0)[0]
except EOFError:
    pass

print(total)
