import sys
import copy

field = [[[] for _ in range(4)] for _ in range(4)]
dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

for i in range(4):
    row = list(map(int,sys.stdin.readline().split()))
    for j in range(4):
        field[i][j] = [row[j*2],row[j*2+1]-1]

max_score = 0

def dfs(sx, sy, score, field):
    global max_score
    score += field[sx][sy][0]
    max_score = max(max_score, score)
    field[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if field[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = field[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dir[nd][0]
            ny = f_y + dir[nd][1]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            field[f_x][f_y][1] = nd
            field[f_x][f_y], field[nx][ny] = field[nx][ny], field[f_x][f_y]
            break

    # 상어 먹음
    s_d = field[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dir[s_d][0]*i
        ny = sy + dir[s_d][1]*i
        if (0<= nx < 4 and 0<= ny < 4) and field[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(field))

dfs(0, 0, 0, field)
print(max_score)
