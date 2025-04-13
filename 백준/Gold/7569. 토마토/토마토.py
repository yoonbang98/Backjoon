import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
field_total = []
for _ in range(H):
    field = [list(map(int, input().split())) for _ in range(N)]
    field_total.append(field)
dir = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def bfs(field_total):
    dist = [[[-1]*M for _ in range(N)] for _ in range(H)]
    queue = deque()
    flag = False
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if field_total[h][r][c] == 1:
                    queue.append([h, r, c])
                    dist[h][r][c] = 0
                if not field_total[h][r][c]:
                    flag = True
    if queue and not flag:
        return 0
    while queue:
        h, r, c = queue.popleft()
        for dh, dr, dc in dir:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0 > nh or H <= nh or 0 > nr or N <= nr or 0 > nc or M <= nc : continue
            if field_total[nh][nr][nc] == 0 and dist[nh][nr][nc] == -1:
                field_total[nh][nr][nc] = 1
                dist[nh][nr][nc] = dist[h][r][c] + 1
                queue.append([nh,nr,nc])
    answer = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if not field_total[h][r][c]: #익지않은 토마토 존재
                    return -1
                if dist[h][r][c] != -1:
                    answer = max(answer, dist[h][r][c])
    return answer
answer = bfs(field_total)
print(answer)