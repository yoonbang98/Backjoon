import sys
from collections import deque
from math import inf
input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(input().strip()) for _ in range(N)]
visited = [[[inf]*M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 1

queue = deque()
queue.append([0,0,0])
dir = [(1,0),(0,1),(-1,0),(0,-1)]
while queue:
    r, c, depth = queue.popleft()
    if r == N-1 and c == M-1:
        break
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if depth == 0 : #아직 안뚫었음
            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == '1' and visited[1][nr][nc] > visited[depth][r][c] + 1:
                    visited[1][nr][nc] = visited[depth][r][c] + 1
                    queue.append([nr,nc,1])
                if field[nr][nc]  == '0' and visited[depth][nr][nc] > visited[depth][r][c] + 1:
                    visited[depth][nr][nc] = visited[depth][r][c] + 1
                    queue.append([nr,nc,0])
        else: #이미 뚫었음
            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == '0' and visited[depth][nr][nc] > visited[depth][r][c] + 1:
                    visited[depth][nr][nc] = visited[depth][r][c] + 1
                    queue.append([nr,nc,1])
answer = min(visited[0][N-1][M-1], visited[1][N-1][M-1])
if answer == inf:
    print(-1)
else:
    print(answer)
