import sys
from collections import deque
def gravity(field):
    field_t = list(map(list, zip(*field)))
    field_g = []
    for col in field_t:
        col_tmp = []
        for letter in col:
            if letter !='.':
                col_tmp.append(letter)
        num_dot = N - len(col_tmp)
        col_tmp = ['.']*num_dot + col_tmp
        field_g.append(col_tmp)
    return list(map(list, zip(*field_g)))
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(r,c,val):
    global visited
    visited[r][c] = True
    queue = deque()
    queue.append((r,c))
    loc = [[r,c]]
    while queue:
        r,c = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and field[nr][nc] == val:
                queue.append((nr,nc))
                visited[nr][nc] = True
                loc.append([nr,nc])
    return loc
N, M = 12, 6
field = []
for _ in range(N):
    row = list(sys.stdin.readline().strip())
    field.append(row)
answer = 0
while True:
    visited = [[False]*M for _ in range(N)]
    flag = False
    total_loc = []
    for r in range(N):
        for c in range(M):
            if field[r][c] != '.' and not visited[r][c]:
                loc = bfs(r,c, field[r][c])
                if len(loc) >= 4:
                    total_loc.extend(loc)
                    flag = True
    for rr, cc in total_loc:
        field[rr][cc] = '.'
    if not flag:
        break
    answer += 1
    field = gravity(field)
print(answer)