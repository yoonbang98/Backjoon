from collections import defaultdict
import copy
N, M, k = map(int, input().split())
dir = [(-1,-1), (-1,0),(1,0),(0,-1),(0,1)] #위, 아래, 왼, 오른
field = [[[] for _ in range(N)] for _ in range(N)]
shark_info = [[] for _ in range(M)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            shark_info[row[j]-1] = [i,j]
            field[i][j].append(row[j]-1)
shark_dir = list(map(int, input().split()))
for m in range(M):
    shark_info[m].append(shark_dir[m])

shark_dir_dict = defaultdict(list)
for m in range(M):
    for _ in range(4):
        shark_dir_dict[m].append(list(map(int, input().split())))
field_smell = [[[] for _ in range(N)] for _ in range(N)]

t = 0
while True:
    new_field = [[[] for _ in range(N)] for _ in range(N)]
    new_field_smell = copy.deepcopy(field_smell)
    new_shark_info = [[] for _ in range(M)]
    for shark_n, shark in enumerate(shark_info):
        if shark:
            r, c, d_tmp = shark
            new_field_smell[r][c] = [shark_n, k]
            flag = False
            for d in shark_dir_dict[shark_n][d_tmp-1]:
                nr, nc = r + dir[d][0], c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < N and not field_smell[nr][nc]: #냄새가 없을 경우

                    if new_field[nr][nc] : #이미 다른 상어가 있을 경우
                        if new_field[nr][nc][0] < shark_n : # 이미 있는 상어가 더 셀 경우
                            pass
                        else: # 새로 들어온 상어가 더 셀 경우
                            new_field_smell[nr][nc] = [shark_n, k]
                            new_shark_info[shark_n] = [nr,nc,d]
                            new_shark_info[new_field[nr][nc][0]] = [] #쫒겨남
                            new_field[nr][nc] = [shark_n]
                    else:
                        new_field_smell[nr][nc] = [shark_n, k]
                        new_shark_info[shark_n] = [nr,nc,d]
                        new_field[nr][nc] = [shark_n]
                    flag = True
                    break
            if not flag: #주변에 빈칸이 없을 경우
                r, c, d_tmp = shark
                for d in shark_dir_dict[shark_n][d_tmp-1]:
                    nr, nc = r + dir[d][0], c + dir[d][1]
                    if 0 <= nr < N and 0 <= nc < N and field_smell[nr][nc][0] == shark_n:
                        new_field_smell[nr][nc] = [shark_n, k]
                        new_shark_info[shark_n] = [nr,nc,d]
                        new_field[nr][nc] = [shark_n]
                        break
    shark_info = new_shark_info
    field = new_field
    field_smell = new_field_smell
    for i in range(N):
        for j in range(N):
            if not field[i][j] and field_smell[i][j]: #상어가 없고 냄새만 있음
                field_smell[i][j][1] -= 1
                if not field_smell[i][j][1]:
                    field_smell[i][j] = []
    # print(field)
    # print(shark_info)
    # print(field_smell)
    t += 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                cnt += 1
    if cnt == 1:
        break
    if t >= 1000:
        t = -1
        break
print(t)