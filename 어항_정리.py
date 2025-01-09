import sys

N, K = map(int, sys.stdin.readline().split())
fish_bowl = list(map(int, sys.stdin.readline().split()))

answer = 0

while True:
    min_val = min(fish_bowl)
    for idx, n in enumerate(fish_bowl):
        if n == min_val:
            fish_bowl[idx] += 1

    dir = [(1,0),(0,1)]
    field = [[0]*N for _ in range(N)]
    field[-1] = fish_bowl
    field[-1][0], field[-2][3] = field[-2][3], field[-1][0]
    field[-1][1], field[-2][2] = field[-2][2], field[-1][1]

    while True:
        tmp = []
        num_1 = 0
        height = 0
        j = 0
        for idx, n in enumerate(field[-1]):
            if n :
                col = []
                for i in range(N):
                    if field[i][idx]:
                        col.append(field[i][idx])
                if len(col) >= 2:
                    height = len(col)
                    tmp.append(col[::-1])
                if len(col) == 1:
                    num_1 += 1
                    if not j :
                        j = idx
        if num_1 >= height:
            new_field = [[0]*N for _ in range(N)]
            new_field[-1][j:] = field[-1][j:]
            h = -2
            start = j
            while tmp:
                tower = tmp.pop()
                for k, t in enumerate(tower):
                    new_field[h][start + k] = t
                h -= 1
            field = new_field
        else:
            break

    subtract_field = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if field[r][c]:
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and field[nr][nc]:
                        d = abs(field[nr][nc] - field[r][c])//5
                        if d :
                            if field[nr][nc] > field[r][c]:
                                subtract_field[nr][nc] -= d
                                subtract_field[r][c] += d
                            else:
                                subtract_field[r][c] -= d
                                subtract_field[nr][nc] += d
    for r in range(N):
        for c in range(N):
            if subtract_field[r][c]:
                field[r][c] += subtract_field[r][c]
    make_1d = []
    for idx, n in enumerate(field[-1]):
        if n :
            col = []
            for i in range(N):
                if field[i][idx]:
                    col.append(field[i][idx])
            make_1d.extend(col[::-1])

    make_2d = []
    make_2d.append(make_1d[:int(N/2)][::-1])
    make_2d.append(make_1d[int(N/2):])

    make_2d_2 = []
    make_2d_2.append(make_2d[-1][:int(N//4)][::-1])
    make_2d_2.append(make_2d[0][:int(N/4)][::-1])
    make_2d_2.append(make_2d[0][int(N/4):])
    make_2d_2.append(make_2d[-1][int(N/4):])

    n_r, n_c = len(make_2d_2), len(make_2d_2[0])
    subtract_make_2d = [[0]*n_c for _ in range(n_r)]

    for r in range(n_r):
        for c in range(n_c):
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n_r and 0 <= nc < n_c:
                    d = abs(make_2d_2[nr][nc] - make_2d_2[r][c]) // 5
                    if d:
                        if make_2d_2[nr][nc] > make_2d_2[r][c]:
                            subtract_make_2d[nr][nc] -= d
                            subtract_make_2d[r][c] += d
                        else:
                            subtract_make_2d[r][c] -= d
                            subtract_make_2d[nr][nc] += d
    for r in range(n_r):
        for c in range(n_c):
            if subtract_make_2d[r][c]:
                make_2d_2[r][c] += subtract_make_2d[r][c]
    final_1d = []
    for c in range(n_c):
        col = [make_2d_2[n][c] for n in range(n_r)]
        final_1d.extend(col[::-1])
    max_val = max(final_1d)
    min_val = min(final_1d)

    answer += 1
    fish_bowl = final_1d
    if (max_val - min_val) <= K:
        break
print(answer)



