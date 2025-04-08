import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
field = []
for _ in range(N):
    row = list(map(int, input().split()))
    field.append(deque(row))
command = []
for _ in range(T):
    xi, di, ki = map(int, input().split())
    command.append([xi, di, ki])
def rotate(field, xi, di, ki):
    for n in range(1, N + 1):
        if not n%xi:
            row = field[n-1]
            if di == 0: #시계방향
                if M - ki > ki:
                    for _ in range(ki):
                        row.rotate(1)
                else:
                    for _ in range(M-ki):
                        row.rotate(-1)
            else: #반시계 방향
                if M - ki > ki:
                    for _ in range(ki):
                        row.rotate(-1)
                else:
                    for _ in range(M-ki):
                        row.rotate(1)
            field[n-1] = row
    return field
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def update(field):
    visited = [[False]*M for _ in range(N)]
    flag = False #인접하면서 수가 같은게 있는지
    for r in range(N):
        for c in range(M):
            if field[r][c]:
                for dr, dc in dir:
                    nr, nc = r + dr, (c + dc)%M
                    if 0 > nr or nr >= N : continue
                    if not field[nr][nc] : continue
                    if field[r][c] == field[nr][nc]:
                        visited[r][c] = True
                        visited[nr][nc] = True
                        flag = True
    if flag:
        for r in range(N):
            for c in range(M):
                if visited[r][c]:
                    field[r][c] = 0
    else:
        sum_tmp = 0
        cnt = 0
        for r in range(N):
            for c in range(M):
                if field[r][c]:
                    sum_tmp += field[r][c]
                    cnt += 1
        if cnt:
            mean_value = sum_tmp/cnt
            for r in range(N):
                for c in range(M):
                    if field[r][c] and field[r][c] > mean_value:
                        field[r][c] -= 1
                    elif field[r][c] and field[r][c] < mean_value:
                        field[r][c] += 1

    return field
for xi, di, ki in command:
    field = rotate(field, xi, di, ki)
    field = update(field)
answer = 0
for row in field:
    answer += sum(row)
print(answer)