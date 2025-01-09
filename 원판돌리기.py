import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(deque(list(map(int, sys.stdin.readline().split()))))
dir = [(0,1), (1,0)]
for _ in range(T):
    x,d,k = map(int, sys.stdin.readline().split())
    for i in range(1,N//x +1):
        if d == 0:
            field[x*i-1].rotate(k)
        else:
            field[x * i - 1].rotate(-k)
    near = [[False]*M for _ in range(N)]
    cnt = 0
    total_sum = 0
    non_zero = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] != 0:
                total_sum += field[r][c]
                non_zero += 1

            for drow, dcol in dir:
                nr = drow + r
                nc = dcol + c
                if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == field[r][c] and field[r][c] != 0:
                    near[r][c] = True
                    near[nr][nc] = True
                    cnt += 1
                if c == M-1 and nc == M and field[nr][0] == field[r][c] and field[r][c] != 0:
                    near[r][c] = True
                    near[nr][0] = True
                    cnt += 1
    if cnt > 0 :
        for r in range(N):
            for c in range(M):
                if near[r][c]:
                    field[r][c] = 0
    elif cnt == 0:
        if total_sum == 0:
            break
        mean = total_sum/non_zero

        for r in range(N):
            for c in range(M):
                if field[r][c] > 0:
                    if field[r][c] > mean:
                        field[r][c] -= 1
                        continue
                    if field[r][c] < mean:
                        field[r][c] += 1
answer = 0
for row in field:
    answer += sum(row)
print(answer)
