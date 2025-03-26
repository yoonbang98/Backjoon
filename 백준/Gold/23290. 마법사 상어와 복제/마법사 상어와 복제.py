import sys
import copy
input = sys.stdin.readline

M, S = map(int, input().split())
field = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fx, fy, d = map(int, input().split())
    field[fx-1][fy-1].append(d-1)

fish_smell = [[0]*4 for _ in range(4)]
shark_r, shark_c = map(int, input().split())
shark_r -= 1
shark_c -= 1
dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
dir2 = [(-1,0),(0,-1),(1,0),(0,1)]
def move_fish(field, fish_smell):
    new_field = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if field[r][c]:
                for d in field[r][c]:
                    cnt = 0
                    fish_d = d
                    while cnt < 8 :
                        nr, nc = r + dir[fish_d][0], c + dir[fish_d][1]
                        if 0 <= nr < 4 and 0 <= nc < 4 and not fish_smell[nr][nc] and (nr, nc) != (shark_r, shark_c):
                            new_field[nr][nc].append(fish_d)
                            break
                        else:
                            cnt += 1
                            fish_d = (fish_d - 1)%8
                    if cnt == 8:
                        new_field[r][c].append(d)
    return new_field
def move_shark(shark_r, shark_c, field, fish_smell):
    candidate = []
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                visited = [[False]*4 for _ in range(4)]
                route = [d1, d2, d3]
                cnt = 0
                flag = True
                r, c = shark_r, shark_c
                for d in route:
                    nr, nc = r + dir2[d][0], c + dir2[d][1]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        if not visited[nr][nc]:
                            cnt += len(field[nr][nc])
                        visited[nr][nc] = True
                        r, c = nr, nc
                    else:
                        flag = False
                        break
                if flag:
                    candidate.append([cnt] + route)

    candidate.sort(key = lambda x : (-x[0], x[1], x[2], x[3]))
    route = candidate[0][1:]
    visited = [[False]*4 for _ in range(4)]
    for d in route:
        shark_r, shark_c = shark_r + dir2[d][0], shark_c + dir2[d][1]
        if field[shark_r][shark_c] and not visited[shark_r][shark_c]:
            fish_smell[shark_r][shark_c] = 3
            field[shark_r][shark_c] = []
        visited[shark_r][shark_c] = True

    return shark_r, shark_c, field, fish_smell



for _ in range(S):
    field_copy = copy.deepcopy(field)
    field = move_fish(field, fish_smell)
    #print(field)
    shark_r, shark_c, field, fish_smell = move_shark(shark_r, shark_c, field, fish_smell)
    #print(shark_r, shark_c, field, fish_smell)
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j]:
                fish_smell[i][j] -= 1
    for i in range(4):
        for j in range(4):
            if field_copy[i][j]:
                field[i][j] = field[i][j] + field_copy[i][j]
    #print(field)
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(field[i][j])
print(answer)