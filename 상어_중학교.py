import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
dir = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(i,j, value):
    total = []
    rainbow = 0
    pivot = []

    visited[i][j] = True
    visited_zero = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append((i,j))
    total.append((i,j))
    pivot.append((i,j))
    while queue:
        r, c = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and field[nr][nc] == value: #일반 블록
                total.append((nr,nc))
                queue.append((nr,nc))
                visited[nr][nc] = True
                pivot.append((nr, nc))
            if 0 <= nr < N and 0 <= nc < N and not visited_zero[nr][nc] and field[nr][nc] == 0: # 무지개 블록
                total.append((nr, nc))
                queue.append((nr, nc))
                rainbow += 1
                visited_zero[nr][nc] = True
    pivot_sorted = sorted(pivot, key = lambda x : (x[0], x[1]))
    return total, rainbow, pivot_sorted[0]
def gravity(a):
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if a[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<N and a[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r+1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break
score = 0
while True:
    visited = [[False] * N for _ in range(N)]
    block = []
    for r in range(N):
        for c in range(N):
            if field[r][c] > 0 and not visited[r][c]:
                total, rainbow, pivot = bfs(r,c, field[r][c])
                if len(total) >= 2:
                    block.append((total, rainbow, pivot))
    if len(block) == 0:
        break
    block_sorted = sorted(block, key = lambda  x : (-len(x[0]), -x[1], - x[2][0], - x[2][1]))

    score += len(block_sorted[0][0])**2
    for r,c in block_sorted[0][0]:
        field[r][c] = -2
    gravity(field)
    field = list(map(list,zip(*field)))[::-1]
    gravity(field)

print(score)