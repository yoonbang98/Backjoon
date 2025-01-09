import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(sys.stdin.readline().strip()))
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(i,j):
    global visited
    visited[i][j] = 0
    queue = deque()
    queue.append((i,j))
    while queue:
        r, c = queue.popleft()
        for dr, dc in dir :
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                if field[nr][nc] == '0':
                    visited[nr][nc] = visited[r][c]
                    queue.appendleft((nr,nc))
                else :
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
visited = [[-1]*M for _ in range(N)]
bfs(0,0)
print(visited[N-1][M-1])