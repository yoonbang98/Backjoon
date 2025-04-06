N, K = map(int, input().split())
flour = list(map(int, input().split()))

def turn_dough(flour):
    field = [[0]*N for _ in range(N)]
    field[-1] = flour
    field[-1][0], field[-2][3] = field[-2][3], field[-1][0]
    field[-1][1], field[-2][2] = field[-2][2], field[-1][1]
    sc = 2
    while True:
        tmp_total = []
        while True:
            tmp = []
            for r in range(N-1, -1 ,-1):
                if field[r][sc]:
                    tmp.append(field[r][sc])
                else:
                    break
            if len(tmp) >= 2:
                tmp_total.append(tmp)
            if len(tmp) == 1:
                break
            sc += 1
            if sc == N - 1:
                break
        if N - sc >= len(tmp_total[0]):
            new_field = [[0]*N for _ in range(N)]
            new_field[-1][sc:] = field[-1][sc:]
            for row_idx, row in enumerate(tmp_total):
                new_field[N-1-len(tmp_total)+row_idx][sc:sc+len(row)] = row
            field = new_field
        else:
            break
    for c_idx in range(N):
        if field[-1][c_idx]:
            break
    for r_idx in range(N):
        if sum(field[r_idx]):
            break
    field_small = []
    for r in range(r_idx, N):
        field_small.append(field[r][c_idx:])
    return field_small
dir = [(1,0),(0,1)]
def push_dough(field):
    N, M = len(field), len(field[0])
    diff_field = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if field[r][c] :
                for dr ,dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 > nr or N <= nr or 0 > nc or M <= nc : continue
                    if not field[nr][nc] : continue
                    diff = abs(field[nr][nc] - field[r][c])//5
                    if not diff : continue
                    if field[nr][nc] > field[r][c]:
                        diff_field[nr][nc] -= diff
                        diff_field[r][c] += diff
                    else:
                        diff_field[nr][nc] += diff
                        diff_field[r][c] -= diff
    for r in range(N):
        for c in range(M):
            if diff_field[r][c]:
                field[r][c] += diff_field[r][c]
    return field
def make_1d(field):
    new_flour = []
    N, M = len(field), len(field[0])
    for c in range(M):
        for r in range(N-1, -1,-1):
            if field[r][c]:
                new_flour.append(field[r][c])
            else:
                break
    return new_flour
min_value, max_value = min(flour), max(flour)
if max_value - min_value <= K:
    print(0)
else:
    answer = 0
    while True:
        min_value, max_value = min(flour), max(flour)
        if max_value - min_value <= K:
            break
        for i, num in enumerate(flour):
            if num == min_value:
                flour[i] += 1
        field = turn_dough(flour)
        field = push_dough(field)
        flour = make_1d(field)
        flour_half = [flour[:N//2][::-1][:], flour[N//2:][:]]
        flour_half_half = [flour_half[1][:N//4][::-1][:], flour_half[0][:N//4][::-1][:],flour_half[0][N//4:][:], flour_half[1][N//4:][:]]
        field = push_dough(flour_half_half)
        flour = make_1d(field)
        answer += 1
    print(answer)
