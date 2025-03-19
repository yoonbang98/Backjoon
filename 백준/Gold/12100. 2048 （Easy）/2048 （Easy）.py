import copy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [0,1,2,3]#상하좌우
li = [[2,-1],[0,1]]
answer = 0
def push_board(board, d):
    if d <= 1: #상하로 이동
        new_board = []
        ro_board = list(map(list, zip(*board[::-1])))
        for row in ro_board:
            row_tmp = []
            cnt = 0
            for num in row:
                if num : row_tmp.append(num)
                if not num : cnt += 1
            if d == 0 :
                row_tmp = [0]*cnt + row_tmp
            elif d == 1:
                row_tmp = row_tmp + [0]*cnt
            new_board.append(row_tmp)
        new_board = list(map(list, zip(*new_board)))[::-1]
    else: #좌우로 이동
        new_board = []
        for row in board:
            row_tmp = []
            cnt = 0
            for num in row:
                if num : row_tmp.append(num)
                if not num : cnt += 1
            if d == 2 :
                row_tmp = row_tmp + [0]*cnt
            elif d == 3:
                row_tmp = [0]*cnt + row_tmp
            new_board.append(row_tmp)
    return new_board

def add_board(board, d):
    N = len(board)
    flag = False
    if d <= 1: #상하로 이동
        ro_board = list(map(list, zip(*board[::-1])))
        if d == 0:
            for i, row in enumerate(ro_board):
                for j in range(N-1, 0, -1):
                    if row[j] and row[j] == row[j-1]:
                        flag = True
                        row[j], row[j-1] = row[j]*2, 0
        if d == 1:
            for i, row in enumerate(ro_board):
                for j in range(N-1):
                    if row[j] and row[j] == row[j+1]:
                        flag = True
                        row[j], row[j+1] = row[j]*2, 0
        new_board = list(map(list, zip(*ro_board)))[::-1]
    else : #좌우로 이동
        if d == 2:
            for i, row in enumerate(board):
                for j in range(N-1):
                    if row[j] and row[j] == row[j+1]:
                        flag = True
                        row[j], row[j+1] = row[j]*2, 0
        if d == 3:
            for i, row in enumerate(board):
                for j in range(N-1, 0, -1):
                    if row[j] and row[j] == row[j-1]:
                        flag = True
                        row[j], row[j-1] = row[j]*2, 0
        new_board = board
    return new_board, flag
def dfs(cnt, board):
    global answer
    if cnt == 5:
        result = 0
        for row in board:
            result = max(max(row), result)
        answer = max(answer, result)
        return
    board_copy = copy.deepcopy(board)
    for d in dir:
        new_board = push_board(board_copy, d)
        new_board, flag = add_board(new_board, d)
        if flag:
            new_board = push_board(new_board, d)
        dfs(cnt + 1, new_board)
    return
dfs(0, board)
print(answer)