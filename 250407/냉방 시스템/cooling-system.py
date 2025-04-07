import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
field = []
aircon = []
target = []
dir = [(0,-1),(-1,0),(0,1),(1,0)] #좌상우하
dir2 = [(1,0),(0,1)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            target.append([i,j])
        elif 2 <= row[j] <= 5 :
            aircon.append([i,j,row[j]-2])
    field.append(row)
wall = set()
for _ in range(M):
    r, c, s = map(int, input().split())
    r -= 1
    c -= 1
    if not s:
        wall.add((r-1,c,r,c))
        wall.add((r,c,r-1,c))
    else:
        wall.add((r,c-1,r,c))
        wall.add((r,c,r,c-1))
def blow_wind(field_cool):
    new_field_cool_total = [[0]*N for _ in range(N)]
    for ar, ac, ad in aircon:
        new_field_cool = [[0]*N for _ in range(N)]
        sr, sc = ar + dir[ad][0], ac + dir[ad][1]
        new_field_cool[sr][sc] = 5
        if ad%2 == 0: #좌우 이동
            cnt = 0
            for _ in range(4):
                if 0 >= sc or sc >= N-1 : break
                for r in range(sr-cnt, sr+cnt + 1):
                    if 0 > r or r >= N : continue
                    if new_field_cool[r][sc]:
                        if (r, sc,r,sc+dir[ad][1]) not in wall:
                            new_field_cool[r][sc+dir[ad][1]] = new_field_cool[r][sc] - 1
                        if r >= 1 and (r-1,sc,r,sc) not in wall and (r-1,sc,r-1,sc+dir[ad][1]) not in wall:
                            new_field_cool[r-1][sc+dir[ad][1]] = new_field_cool[r][sc] - 1
                        if r <= N - 2 and (r+1,sc,r,sc) not in wall and (r+1,sc,r+1,sc+dir[ad][1]) not in wall:
                            new_field_cool[r+1][sc+dir[ad][1]] = new_field_cool[r][sc] - 1
                sc += dir[ad][1]
                cnt += 1
        else :
            cnt = 0
            for _ in range(4):
                if 0 >= sr or sr >= N-1 : break
                for c in range(sc-cnt, sc+cnt + 1):
                    if 0 > c or c >= N : continue
                    if new_field_cool[sr][c]:
                        if (sr, c, sr + dir[ad][0],c) not in wall:
                            new_field_cool[sr + dir[ad][0]][c] = new_field_cool[sr][c] - 1
                        if c >= 1 and (sr,c,sr,c-1) not in wall and (sr,c-1,sr+ dir[ad][0],c-1) not in wall:
                            new_field_cool[sr + dir[ad][0]][c-1] = new_field_cool[sr][c] - 1
                        if c <= N - 2 and (sr,c,sr,c+1) not in wall and (sr,c+1,sr+ dir[ad][0],c+1) not in wall:
                            new_field_cool[sr + dir[ad][0]][c+1] = new_field_cool[sr][c] - 1
                sr += dir[ad][0]
                cnt += 1
        for i in range(N):
            for j in range(N):
                if new_field_cool[i][j]:
                    new_field_cool_total[i][j] += new_field_cool[i][j]
    for i in range(N):
        for j in range(N):
            new_field_cool_total[i][j] += field_cool[i][j]
    return new_field_cool_total
def mix_wind(field_cool):
    field_diff = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for dr, dc in dir2:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                if (r,c,nr,nc) in wall : continue
                diff = int(abs(field_cool[nr][nc]- field_cool[r][c])/4)
                if not diff: continue
                if field_cool[nr][nc] > field_cool[r][c]:
                    field_diff[nr][nc] -= diff
                    field_diff[r][c] += diff
                else:
                    field_diff[nr][nc] += diff
                    field_diff[r][c] -= diff
    for r in range(N):
        for c in range(N):
            if field_diff[r][c]:
                field_cool[r][c] += field_diff[r][c]
    return field_cool
t = 0
field_cool = [[0]*N for _ in range(N)]
while True:
    flag = True
    for t_r, t_c in target:
        if field_cool[t_r][t_c] < K:
            flag = False
            break
    if flag:
        break
    if t > 100 :
        t = -1
        break
    field_cool = blow_wind(field_cool)
    field_cool = mix_wind(field_cool)

    for r in range(N):
        if field_cool[r][0]:
            field_cool[r][0] -= 1
        if field_cool[r][N-1]:
            field_cool[r][N-1] -= 1
    for c in range(1,N-1):
        if field_cool[0][c]:
            field_cool[0][c] -= 1
        if field_cool[N-1][c]:
            field_cool[N-1][c] -= 1
    t += 1
print(t)