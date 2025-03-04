import copy
from math import inf
dir = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
dir_list = [[], [[0], [1], [2], [3]],
            [[0,1],[2,3]], [[0,2],[1,3],[1,2],[0,3]],
            [[0,1,2],[0,1,3],[0,2,3],[1,2,3]], [[0,1,2,3]]]
field = []
cctv = []
N, M = map(int, input().split())

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctv.append([i,j,row[j]])
    field.append(row)
answer = inf
def watch(sr,sc, d_list, field):
    for d in d_list:
        r = sr
        c = sc
        while True:
            nr, nc = r + dir[d][0], c + dir[d][1]
            if 0 > nr or N <= nr or 0 > nc or M <= nc:
                break
            if field[nr][nc] == 6:
                break
            if not field[nr][nc] :
                field[nr][nc] = -1
            r, c = nr, nc
    return field
def dfs(cnt, field):
    global answer
    if cnt == len(cctv):
        result = 0
        for i in range(N):
            for j in range(M):
                if not field[i][j]:
                    result+=1
        answer = min(answer, result)
        return
    r, c, n = cctv[cnt]
    possible_dir = dir_list[n]
    for d_list in possible_dir:
        field_copy = copy.deepcopy(field)
        new_field = watch(r, c, d_list, field_copy)
        dfs(cnt + 1, new_field)
    return
dfs(0, field)
print(answer)