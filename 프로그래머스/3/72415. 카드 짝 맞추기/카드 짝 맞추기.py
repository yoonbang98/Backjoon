from copy import deepcopy
from math import inf
from collections import deque

def get_key_count(board, cy, cx, ty, tx):
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]
    que = deque()
    que.append((cy, cx))
    visited = [[inf for _ in range(4)] for _ in range(4)]
    visited[cy][cx] = 0
    while que:
        y, x = que.popleft()
        if y == ty and x == tx:
            return visited[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((ny, nx))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            while 0 <= ny + dy[i] < 4 and 0 <= nx + dx[i] < 4 and board[ny][nx] == 0:
                ny, nx = ny + dy[i], nx + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((ny, nx))


# # test
# board = [[1,0,0,3],[0,0,0,0],[0,0,0,2],[3,0,1,0]]
# print(get_key_count(board, 0, 3, 0 ,3))

def get_coord_by_num(board, target):
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                return i, j

answer = inf

def is_end(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    return True


def dfs(board, r, c, ty1, tx1, cnt):
    global answer
    board = deepcopy(board)
    target_num = board[ty1][tx1]

    # 첫 번째 카드
    cnt += get_key_count(board, r, c, ty1, tx1)
    board[ty1][tx1] = 0
    # 두 번째 카드
    ty2, tx2 = get_coord_by_num(board, target_num)
    cnt += get_key_count(board, ty1, tx1, ty2, tx2)
    board[ty2][tx2] = 0
    cnt += 2
    if is_end(board):
        answer = min(answer, cnt)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, ty2, tx2, i, j, cnt)

def solution(board, r, c):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, r, c, i, j, 0)

    return answer