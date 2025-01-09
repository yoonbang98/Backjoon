import sys
from collections import deque

N = int(sys.stdin.readline())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
visited = [[False]*N for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(i,j, num):
    visited[i][j] = True
    queue = deque()
    queue.append((i,j))
    field[i][j] = num
    while queue:
        r, c = queue.popleft()
        cnt = 0
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and field[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                field[nr][nc] = num
                queue.append((nr,nc))
            if 0 <= nr < N and 0 <= nc < N and field[nr][nc] == 0:
                cnt += 1
        if cnt :
            total_corner.append((r,c))
def TaxiDistance(y, x):
    val = field[y][x]
    visited = set([(y, x)])
    queue = deque([(y, x, 0)])
    while queue:
        y, x, dist = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                if field[ny][nx] and field[ny][nx] != val:
                    return dist
                visited.add((ny, nx))
                queue.append((ny, nx, dist + 1))
total_corner = []
num = 2
for r in range(N):
    for c in range(N):
        if field[r][c] and not visited[r][c]:
            bfs(r,c, num)
            num += 1

answer = 1e9
for i, j in total_corner:
    answer = min(answer, TaxiDistance(i,j))
print(answer)