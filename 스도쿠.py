# import sys
#
# sudoku = []
# zero = []
# for _ in range(9):
#     line = list(map(int , sys.stdin.readline().strip()))
#     sudoku.append(line)
# answer = []
# for r in range(9):
#     for c in range(9):
#         if not sudoku[r][c]:
#             zero.append([r,c])
#
# def dfs(sudoku, cnt):
#     if cnt == len(zero):
#         answer.append(sudoku)
#         return
#     #print(cnt)
#     r = zero[cnt][0]
#     c = zero[cnt][1]
#     set_r = set(sudoku[r])
#     set_c = set([sudoku[n][c] for n in range(9)])
#     nemo = []
#     for row in range(r // 3, r // 3 + 3):
#         nemo.extend(sudoku[row][c // 3:c // 3 + 3])
#     total_set = set(nemo).union(set_r).union(set_c)
#     print(total_set)
#     for num in range(1, 10):
#         if num not in total_set:
#             sudoku[r][c] = num
#             dfs(sudoku, cnt + 1)
#             sudoku[r][c] = 0
# dfs(sudoku, 0)
# print(answer)

import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int , sys.stdin.readline().strip().split())))
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
            #print(''.join(map(str, graph[i])))
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0
dfs(0)