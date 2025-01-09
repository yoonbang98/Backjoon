import sys
from collections import deque
from itertools import combinations
import copy

N, M = map(int, sys.stdin.readline().split())
field = []
diffusion_field = [[-1]*N for _ in range(N)]
virus = []
num_blank = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    field.append(row)
    for j in range(N):
        if row[j] == 1:
            diffusion_field[i][j] = '-'
        elif row[j] == 2:
            virus.append((i,j))
        else:
            num_blank += 1
dir = [(0,1),(1,0),(-1,0),(0,-1)]
answer = 1000000
for com in combinations(virus, M):
    tmp_field = copy.deepcopy(diffusion_field)
    active = deque(com)
    not_active = set(virus)-set(com)
    for r,c, in not_active:
        tmp_field[r][c] = '*'
    for r,c, in active:
        tmp_field[r][c] = 0
    cnt = 0
    time = 0
    while active:
        r,c = active.popleft()
        for drow, dcol in dir:
            nr = r + drow
            nc = c + dcol
            if 0 <= nr < N and 0 <= nc < N and (tmp_field[nr][nc] == -1 or tmp_field[nr][nc] == '*'):
                if tmp_field[nr][nc] == -1:
                    cnt += 1
                    tmp_field[nr][nc] = tmp_field[r][c] + 1
                    time = max(time, tmp_field[nr][nc])
                else :
                    tmp_field[nr][nc] = tmp_field[r][c] + 1
                active.append((nr,nc))

    if num_blank == cnt:
        answer = min(answer, time)
    else :
        continue
if answer == 1000000:
    print(-1)
else :
    print(answer)


