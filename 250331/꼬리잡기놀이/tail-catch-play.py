import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
head = []
field = []
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            head.append([row[c], r, c])
    field.append(row)
dir = [(1,0),(0,1),(-1,0),(0,-1)]
group_total = []
for num, r, c in head:
    group = []
    group.append([num, r, c])
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    queue.append([r,c])
    visited[r][c] = True
    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in dir:
            nr, nc = dr + cur_r, dc + cur_c
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if field[cur_r][cur_c] == 1 and field[nr][nc] == 3: continue
                if 2 <= field[nr][nc] <= 3:
                    queue.append([nr,nc])
                    visited[nr][nc] = True
                    group.append([field[nr][nc], nr, nc])
    group_total.append(group)
def move(field, group_total):
    new_group_total = []
    visited = [[False]*N for _ in range(N)]
    for group in group_total:
        new_group = []
        for num, r, c in group:
            visited[r][c] = True
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N : continue
                if num == 1 and field[nr][nc] >= 3: #머리이동
                    new_group.append([num, nr, nc])
                    field[nr][nc], field[r][c] = field[r][c], field[nr][nc]
                    break
                elif visited[nr][nc] and field[nr][nc] >= 3:
                    new_group.append([num, nr, nc])
                    if num == 3 and field[r][c] == 1:
                        continue
                    field[nr][nc], field[r][c] = field[r][c], field[nr][nc]
                    break
        new_group_total.append(new_group)
    return field, new_group_total
def throw_ball(field, group_total):
    round = k
    round %= (4*N)
    d = int(round//N)
    if d == 0:
        sr, sc = round%N, 0
    elif d == 1:
        sr, sc = N-1, (round-N)%N
    elif d == 2:
        sr, sc = N - 1- (round - 2*N)%N, N-1
    else:
        sr, sc = 0, N -1 - (round - 3*N)%N
    flag = False
    while True:
        if 1 <= field[sr][sc] <= 3:
            flag = True
            break
        sr += dir2[d][0]
        sc += dir2[d][1]
        if sr < 0 or sr >= N or sc < 0 or sc >= N :
            break
    if not flag:
        return field, group_total, 0
    new_group_total = []
    score = 0
    for group in group_total:
        new_group = []
        flag = False
        for idx, (num, r, c) in enumerate(group):
            if (r,c) == (sr, sc):
                flag = True
                score = (idx + 1)**2
            new_group.append([num, r, c])
        if flag:
            new_group = new_group[::-1]
            new_group[0][0] = 1
            new_group[-1][0] = 3
            field[new_group[0][1]][new_group[0][2]] = 1
            field[new_group[-1][1]][new_group[-1][2]] = 3
        new_group_total.append(new_group)
    return field, new_group_total, score
dir2 = [(0,1),(-1,0),(0,-1),(1,0)]#우상좌하
answer = 0
for k in range(K):
    field, group_total = move(field, group_total)
    field, group_total, score = throw_ball(field, group_total)
    answer += score
print(answer)