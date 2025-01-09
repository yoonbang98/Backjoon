import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs_blank(i,j):
    visited_blank[i][j] = True
    queue = deque()
    queue.append((i,j))
    while queue:
        r,c = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 0 and not visited_blank[nr][nc]:
                queue.append((nr,nc))
                visited_blank[nr][nc] = True
def bfs_cheese(i,j):
    visited_cheese[i][j] = True
    queue = deque()
    queue.append((i,j))
    while queue:
        r,c = queue.popleft()
        if field[r][c]:
            cnt = 0
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 0 and visited_blank[nr][nc]:
                    cnt += 1
            if cnt >= 2:
                c_list.append((r,c))
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited_cheese[nr][nc]:
                queue.append((nr,nc))
                visited_cheese[nr][nc] = True


t = 0
while True:
    tmp = 0
    for row in field:
        tmp += sum(row)
    if not tmp:
        break
    visited_blank = [[False]*M for _ in range(N)]
    bfs_blank(0,0)
    c_list = []

    visited_cheese = copy.deepcopy(visited_blank)

    for r in range(N):
        for c in range(M):
            if field[r][c]:
                bfs_cheese(r,c)
    for r,c in set(c_list):
        field[r][c] = 0
    t += 1
print(t)

