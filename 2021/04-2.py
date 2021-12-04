# Read numbers to draw
nums = list(map(int, input().split(",")))
input()

# Read set of boards
board_list = []
board = []

try:
    while True:
        line = input()

        if not line:
            board_list.append(board)
            board = []
        else:
            board.append(list(map(int, line.split())))
except EOFError:
    pass

board_list.append(board)
markers_list = [[[False] * len(bline) for bline in board] for board in board_list]
finis = [False] * len(board_list)

def find_winning_board():
    for num in nums:
        for i, (board, markers) in enumerate(zip(board_list, markers_list)):
            for bline, mline in zip(board, markers):
                try:
                    j = bline.index(num)
                    mline[j] = True
                except ValueError:
                    pass

                # Winning line
                if all(mline):
                    finis[i] = True

                    if all(finis):
                        return (i, num)

            # Winning column
            for k in range(len(board[0])):
                if all(mline[k] for mline in markers):
                    finis[i] = True

                    if all(finis):
                        return (i, num)

# Compute score
winning, num = find_winning_board()
score = 0

for bline, mline in zip(board_list[winning], markers_list[winning]):
    for bnum, mval in zip(bline, mline):
        if not mval:
            score += bnum

print(score * num)
