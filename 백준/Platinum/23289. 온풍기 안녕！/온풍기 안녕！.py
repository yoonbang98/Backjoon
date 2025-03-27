import sys
from math import floor

input = sys.stdin.readline
R, C, K = map(int, input().split())
field_temp = [[0]*C for _ in range(R)]
heater = []
target = []
field_wall = set()

for r in range(R):
    row = list(map(int, input().split()))
    for c in range(C):
        if row[c] == 5:
            target.append([r,c])
        elif row[c]:
            heater.append([r,c,row[c]])
W = int(input())
for _ in range(W):
    wr, wc, t = map(int, input().split())
    wr -= 1
    wc -= 1
    if t == 0:
        field_wall.add((wr, wc, wr-1, wc))
        field_wall.add((wr-1, wc, wr, wc))
    else:
        field_wall.add((wr, wc, wr, wc+1))
        field_wall.add((wr, wc+1, wr, wc))

chocolate = 0
dir = [(-1,-1),(0,1),(0,-1),(-1,0),(1,0)]
def heat(field_temp):
    for hr, hc, d in heater:
        visited = [[0]*C for _ in range(R)]
        sr, sc = hr + dir[d][0], hc + dir[d][1]
        if sr < 0 or sr >= R or sc < 0 or sc >= C: continue
        field_temp[sr][sc] += 5
        visited[sr][sc] = 1
        if 3 <= d <= 4: #히터 방향 위아래일 경우
            temp = 4
            while temp >= 1:
                sr += dir[d][0]
                if sr < 0 or sr >= R : break
                l = 5 - temp
                for c in range(sc-l, sc+l+1):
                    if 0 <= c < C:
                        sr_prev = sr - dir[d][0]
                        if visited[sr_prev][c] and (sr_prev, c, sr, c) not in field_wall:
                            visited[sr][c] = True
                            field_temp[sr][c] += temp
                        elif 0 <= c-1 and visited[sr_prev][c-1] and (sr_prev, c, sr, c) not in field_wall and (sr_prev, c-1, sr_prev, c) not in field_wall:
                            visited[sr][c] = True
                            field_temp[sr][c] += temp
                        elif c+1 < C and visited[sr_prev][c+1] and (sr_prev, c, sr, c) not in field_wall and (sr_prev, c+1, sr_prev, c) not in field_wall:
                            visited[sr][c] = True
                            field_temp[sr][c] += temp
                temp -= 1
        else : #히터 방향 좌우일 경우
            temp = 4
            while temp >= 1:
                sc += dir[d][1]
                if sc < 0 or sc >= C : break
                l = 5 - temp
                for r in range(sr-l, sr+l+1):
                    if 0 <= r < R:
                        sc_prev = sc - dir[d][1]
                        if visited[r][sc_prev] and (r, sc_prev, r, sc) not in field_wall:
                            visited[r][sc] = True
                            field_temp[r][sc] += temp
                        elif 0 <= r-1 and visited[r-1][sc_prev] and (r, sc_prev, r, sc) not in field_wall and (r-1, sc_prev, r, sc_prev) not in field_wall:
                            visited[r][sc] = True
                            field_temp[r][sc] += temp
                        elif r+1 < R and visited[r+1][sc_prev] and (r, sc_prev, r, sc) not in field_wall and (r+1, sc_prev, r, sc_prev) not in field_wall:
                            visited[r][sc] = True
                            field_temp[r][sc] += temp
                temp -= 1
    return field_temp
dir2 = [(1,0),(0,1)]

def temp_adjust(field_temp):
    field_adj = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for dr, dc in dir2:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                diff = floor(abs(field_temp[nr][nc]-field_temp[r][c])/4)
                if not diff or (nr, nc, r, c) in field_wall: continue
                if field_temp[nr][nc] > field_temp[r][c]:
                    field_adj[nr][nc] -= diff
                    field_adj[r][c] += diff
                else:
                    field_adj[nr][nc] += diff
                    field_adj[r][c] -= diff
    for r in range(R):
        for c in range(C):
            field_temp[r][c] += field_adj[r][c]
    return field_temp

while True:
    field_temp = heat(field_temp)
    field_temp = temp_adjust(field_temp)
    for r in range(R):
        if field_temp[r][0]:
            field_temp[r][0] -= 1
        if field_temp[r][C-1]:
            field_temp[r][C-1] -= 1
    for c in range(1, C-1):
        if field_temp[0][c]:
            field_temp[0][c] -= 1
        if field_temp[R-1][c]:
            field_temp[R-1][c] -= 1
    chocolate += 1
    if chocolate > 100:
        break
    flag = True
    for tr, tc in target:
        if field_temp[tr][tc] < K:
            flag = False
            break
    if flag:
        break
if chocolate > 100:
    print(101)
else:
    print(chocolate)
