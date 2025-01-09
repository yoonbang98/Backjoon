import sys
import copy
N, M, k = map(int, sys.stdin.readline().split())
field = []
field_smell = [[[0,0]for _ in range(N)] for _ in range(N)]
for r in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(N):
        if row[c] > 0:
            field_smell[r][c] = [row[c], k]
    field.append(row)
dir = [[],[-1,0],[1,0],[0,-1],[0,1]]
shark_direction = [0] + list(map(int, sys.stdin.readline().split()))
shark_dir_priority = [[[]] for _ in range(M+1)]
for i in range(1,M+1):
    for _ in range(4):
        shark_dir_priority[i].append(list(map(int, sys.stdin.readline().split())))
t = 0
while True:
    field_copy = copy.deepcopy(field)
    for r in range(N):
        for c in range(N):
            if field[r][c] > 0:
                shark = field[r][c]
                shark_d = shark_direction[shark]
                shark_d_p = shark_dir_priority[shark][shark_d]
                move = False
                for d in shark_d_p:
                    dr, dc = dir[d]
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N and field_smell[nr][nc] == [0,0]: #아무 냄새가 없는 칸
                        if field_copy[nr][nc] == 0:
                            field_copy[nr][nc] = shark
                            shark_direction[shark] = d
                            field_copy[r][c] = 0
                            move = True
                            break
                        else:
                            if field_copy[nr][nc] > shark:
                                field_copy[nr][nc] = shark
                                shark_direction[shark] = d
                            field_copy[r][c] = 0
                            move = True
                            break
                if not move:
                    for d in shark_d_p:
                        dr, dc = dir[d]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and field_smell[nr][nc][0] == shark:
                            field_copy[nr][nc] = shark
                            shark_direction[shark] = d
                            field_copy[r][c] = 0
                            break
    field = field_copy
    for r in range(N):
        for c in range(N):
            if field[r][c] == 0 and field_smell[r][c] != [0,0]:
                if field_smell[r][c][1] == 1:
                    field_smell[r][c] = [0,0]
                else:
                    field_smell[r][c] = [field_smell[r][c][0] , field_smell[r][c][1]-1]
            if field[r][c] > 0:
                field_smell[r][c] = [field[r][c], k]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if field[r][c]:
                cnt += 1
            if cnt >= 2:
                break
    t += 1
    if cnt == 1:
        break
    if t >= 1000:
        t = -1
        break
print(t)