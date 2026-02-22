import sys
def winner(board):
    x_win, o_win = False, False
    for line in board:
        if line == ['X'] * len(board):
            x_win = True
        if line == ['O'] * len(board):
            o_win = True
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[2][0] == board[1][1] == board[0][2] == 'O':
        o_win = True
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[2][0] == board[1][1] == board[0][2] == 'X':
        x_win = True
    turn_board = list(map(list, zip(*board)))[::-1]
    for line in turn_board:
        if line == ['X'] * len(board):
            x_win = True
        if line == ['O'] * len(board):
            o_win = True
    return x_win, o_win
while True:
    answer = 'valid'
    result = list(sys.stdin.readline().strip())
    if result == ['e', 'n', 'd']: break
    x_cnt, o_cnt = 0,0
    for re in result:
        if re == 'X':
            x_cnt += 1
        elif re == 'O':
            o_cnt += 1
    if abs(x_cnt - o_cnt) >= 2 or x_cnt < o_cnt:
        answer = 'invalid'
        print(answer)
        continue

    board = [result[0:3], result[3:6], result[6:]]
    x_win, o_win = winner(board)
    if x_win and o_win :
        answer = 'invalid'
    if x_win and not o_win:
        if x_cnt <= o_cnt:
            answer = 'invalid'
    if not x_win and o_win:
        if x_cnt > o_cnt:
            answer = 'invalid'
    if not x_win and not o_win:
        if x_cnt + o_cnt != 9:
            answer = 'invalid'
    print(answer)
