import sys
import copy
M, S = map(int, sys.stdin.readline().split())
field = [[[] for _ in range(4)] for _ in range(4)]
field_smell = [[0]*4 for _ in range(4)]
dir_fish = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
dir_shark = [[-1,0],[0,-1],[1,0],[0,1]]
for _ in range(M):
    fx,fy,d = map(int, sys.stdin.readline().split())
    field[fx-1][fy-1].append(d-1)
shark_r, shark_c = map(int, sys.stdin.readline().split())
shark_r -= 1; shark_c -= 1

def move_fish():
    new_field = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if field[i][j]:
                for d in field[i][j]:
                    cur_d = d
                    cnt = 0
                    while cnt != 8:
                        nr, nc = i + dir_fish[cur_d][0], j + dir_fish[cur_d][1]
                        if 0 <= nr < 4 and 0 <= nc < 4 and not (nr,nc) == (shark_r,shark_c) and not field_smell[nr][nc]:
                            new_field[nr][nc].append(cur_d)
                            break
                        else:
                            cnt += 1
                            cur_d = (cur_d - 1)%8
                    if cnt == 8:
                        new_field[i][j].append(d)
    return new_field
def move_shark(shark_r, shark_c):
    global field
    global field_smell
    result = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                visited = [[0]*4 for _ in range(4)]
                r,c = shark_r, shark_c
                move = [i,j,k]
                num_fish = 0
                flag = True
                for d in move:
                    nr, nc = r + dir_shark[d][0], c + dir_shark[d][1]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        r,c = nr, nc
                        if not visited[nr][nc] and field[nr][nc]:
                            num_fish += len(field[nr][nc])
                        visited[nr][nc] = 1
                    else :
                        flag = False
                if flag:
                    result.append([num_fish, (i+1)*100 + (j+1)*10 + k+1])
    result.sort(key=lambda x: (-x[0], x[1]))
    i,j,k = int(str(result[0][1])[0])-1, int(str(result[0][1])[1])-1,int(str(result[0][1])[2])-1
    move = [i,j,k]
    r, c = shark_r, shark_c
    for d in move:
        nr, nc = r + dir_shark[d][0], c + dir_shark[d][1]
        if field[nr][nc] :
            field[nr][nc] = []
            field_smell[nr][nc] = 3
        r, c = nr, nc
    return r,c
for _ in range(S):
    field_copy = copy.deepcopy(field)
    field = move_fish()

    shark_r, shark_c = move_shark(shark_r, shark_c)
    for i in range(4):
        for j in range(4):
            if field_smell[i][j]:
                field_smell[i][j] -= 1

    for i in range(4):
        for j in range(4):
            if field_copy[i][j]:
                field[i][j].extend(field_copy[i][j])

answer = 0
for i in range(4):
    for j in range(4):
        if field[i][j]:
            answer += len(field[i][j])
print(answer)