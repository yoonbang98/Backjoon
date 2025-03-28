import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def find_block(field):
    visited = [[False]*N for _ in range(N)] #일반 블록만
    result = []
    for r in range(N):
        for c in range(N):
            if field[r][c] >= 1 and not visited[r][c]:
                visited_zero = [[False]*N for _ in range(N)] # 무지개 블록만
                tmp = [r,c]
                queue = deque()
                queue.append([r,c,field[r][c]])
                num = field[r][c]
                cnt_size, cnt_rainbow = 0, 0
                while queue:
                    cur_r, cur_c, cur_num = queue.popleft()
                    for dr, dc in dir:
                        nr, nc = cur_r + dr, cur_c + dc
                        if 0 > nr or nr >= N or 0 > nc or nc >= N : continue
                        if visited[nr][nc] : continue
                        if visited_zero[nr][nc] : continue
                        if field[nr][nc] == 0:#무지개 블록
                            cnt_size += 1
                            cnt_rainbow += 1
                            visited_zero[nr][nc] = True
                            queue.append([nr, nc, field[nr][nc]])
                        elif field[nr][nc] == num:
                            cnt_size += 1
                            visited[nr][nc] = True
                            queue.append([nr, nc, field[nr][nc]])
                if cnt_size >= 2:
                    result.append([cnt_size, cnt_rainbow] + tmp)
    if not result:
        return []
    result.sort(key = lambda x : (-x[0],-x[1],-x[2],-x[3]))
    return result[0]
def bfs(field, r, c):
    queue = deque()
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    num = field[r][c]
    queue.append([r,c])
    while queue:
        r, c = queue.popleft()
        field[r][c] = -2
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 > nr or nr >= N or 0 > nc or nc >= N : continue
            if visited[nr][nc] : continue
            if field[nr][nc] == 0 or field[nr][nc] == num:
                visited[nr][nc] = True
                queue.append([nr,nc])
    return field
def gravity(field):
    for c in range(N):
        for r in range(N-2, -1, -1):
            if field[r][c] >= 0: #일반블록이면
                sr = r
                while True:
                    if sr + 1 <= N - 1 and field[sr+1][c] == -2:
                        field[sr][c], field[sr+1][c] = field[sr+1][c], field[sr][c]
                        sr += 1
                    else :
                        break
    return field
answer = 0
while True:
    block = find_block(field)
    if not block:
        break
    answer += block[0]**2
    field = bfs(field, block[2], block[3])
    field = gravity(field)
    field = list(map(list, zip(*field)))[::-1]
    field = gravity(field)
print(answer)
