import sys
input = sys.stdin.readline
N, M, K, C = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
field_chem = [[0]*N for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def tree_grow(field):
    new_field = [[0]*N for _ in range(N)]
    # 트리 성장
    for r in range(N):
        for c in range(N):
            if field[r][c] == -1:
                new_field[r][c] = -1
                continue
            if field[r][c]:
                cnt = 0
                for dr ,dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 > nr or N <= nr or 0 > nc or N <= nc: continue
                    if field[nr][nc] >= 1:
                        cnt += 1
                new_field[r][c] = field[r][c] + cnt
    #트리 번식
    new_field_copy = [row[:] for row in new_field]
    for r in range(N):
        for c in range(N):
            if new_field[r][c] >= 1:
                cnt = 0
                for dr ,dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 > nr or N <= nr or 0 > nc or N <= nc: continue
                    if not new_field[nr][nc] and not field_chem[nr][nc]:
                        cnt += 1
                if cnt:
                    for dr ,dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 > nr or N <= nr or 0 > nc or N <= nc: continue
                        if not new_field[nr][nc] and not field_chem[nr][nc]:
                            new_field_copy[nr][nc] += int(new_field[r][c]//cnt)
    return new_field_copy
c_dir = [(1,1),(1,-1),(-1,1),(-1,-1)]
def tree_chem(field, field_chem):
    result = []
    for r in range(N):
        for c in range(N):
            if not field[r][c] or field[r][c] == -1:
                result.append([0, r, c])
            else :
                result_tmp = field[r][c]
                for dr, dc in c_dir:
                    sr, sc = r, c
                    cnt = 0
                    while True:
                        nr, nc = sr + dr, sc + dc
                        if 0 > nr or N <= nr or 0 > nc or N <= nc: break
                        cnt += 1
                        if not field[nr][nc] or field[nr][nc] == -1:
                            break
                        result_tmp += field[nr][nc]
                        if cnt == K :
                            break
                        sr, sc = nr, nc
                result.append([result_tmp, r, c])
    result.sort(key = lambda x : (-x[0], x[1], x[2]))
    r, c = result[0][1], result[0][2]
    if result[0][0]:
        field[r][c] = 0
        field_chem[r][c] = C + 1
        for dr, dc in c_dir:
            sr, sc = r, c
            cnt = 0
            while True:
                nr, nc = sr + dr, sc + dc
                if 0 > nr or N <= nr or 0 > nc or N <= nc: break
                cnt += 1
                if not field[nr][nc] or field[nr][nc] == -1:
                    field_chem[nr][nc] = C + 1
                    break
                field[nr][nc] = 0
                field_chem[nr][nc] = C + 1
                if cnt == K :
                    break
                sr, sc = nr, nc
    else:
        field_chem[r][c] = C+1
    return field, field_chem, result[0][0]


answer = 0
for _ in range(M):
    field = tree_grow(field)
    field, field_chem, num_tree = tree_chem(field, field_chem)
    answer += num_tree
    for r in range(N):
        for c in range(N):
            if field_chem[r][c]:
                field_chem[r][c] -= 1
print(answer)