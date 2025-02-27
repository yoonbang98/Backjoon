import copy
dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
field = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        field[i][j] = [row[j*2], row[j*2+1]-1]

shark_r, shark_c = 0,0
answer = field[shark_r][shark_c][0]
shark_d = field[shark_r][shark_c][1]
field[shark_r][shark_c] = []

def fish_move(field, shark_r, shark_c):
    for num in range(1,17):
        for i in range(4):
            flag = False
            for j in range(4):
                if field[i][j] and field[i][j][0] == num:
                    d = field[i][j][1]
                    cnt = 0
                    while True:
                        if cnt == 8 :
                            break
                        nr, nc = i + dir[d][0], j + dir[d][1]
                        if 0 > nr or nr >= 4 or 0 > nc or nc >= 4:
                            d = (d+1)%8
                            cnt += 1
                            continue
                        if shark_r == nr and shark_c == nc:
                            d = (d+1)%8
                            cnt += 1
                            continue
                        if not field[nr][nc]:
                            field[i][j] = []
                            field[nr][nc] = [num, d]
                            break
                        else:
                            tmp = field[nr][nc]
                            field[nr][nc] = [num, d]
                            field[i][j] = tmp
                            break
                    flag = True
                    break
            if flag:
                break
    return field
def dfs(shark_r, shark_c, shark_d, result, field):
    global answer
    sr, sc = shark_r, shark_c
    field = copy.deepcopy(field)
    field = fish_move(field, shark_r, shark_c)

    next_loc = []
    while True:
        nr, nc = sr + dir[shark_d][0], sc + dir[shark_d][1]
        if 0 > nr or nr >= 4 or 0 > nc or nc >= 4:
            break
        if field[nr][nc]:
            next_loc.append([nr, nc])
        sr, sc = nr, nc
    if not next_loc:
        answer = max(answer, result)
        return
    for nr, nc in next_loc:
        tmp = field[nr][nc]
        field[nr][nc] = []
        dfs(nr, nc, tmp[1], result + tmp[0], field)
        field[nr][nc] = tmp
    return
dfs(shark_r, shark_c, shark_d, answer, field)

print(answer)