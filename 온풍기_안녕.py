import sys

R,C,K = map(int, sys.stdin.readline().split())
warm = []
invest = []
for r in range(R):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(C):
        if row[c] and row[c] < 5:
            warm.append([r,c,row[c]])
        elif row[c]:
            invest.append([r,c])
field = [[0]*C for _ in range(R)]
W = int(sys.stdin.readline())
wall = []
for _ in range(W):
    x, y, t = map(int, sys.stdin.readline().split())
    wall.append([x-1,y-1,t])
dir = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
for s_r, s_c, d in warm:
    next_tmp = []
    if d == 4 and s_r+1 < R and [s_r+1,s_c,0] not in wall:
        field[s_r+1][s_c] += 5
        next_tmp.append([s_r+1, s_c, 5])
    for _ in range(4):
        if d == 4:
            next_next_tmp = []
            while next_tmp:
                r,c,val = next_tmp.pop()
                nr, nc = r + dir[d], c + dir[d]
                if 0 <= nr < R and 0 <= nc < C and [nr,nc,0] not in wall:
                    field[nr][nc] += val-1
                    next_next_tmp.append([nr, nc, val-1])
                if 0 <= nr < R and 0 <= nc < C and [nr, nc-1, 0] not in wall and [nr, nc-1, 1]:
                    field[nr][nc-1] += val - 1
                    next_next_tmp.append([nr, nc-1, val - 1])
                if 0 <= nr < R and 0 <= nc < C and [nr, nc+1, 0] not in wall and [nr, nc-1, 1]:
                    field[nr][nc-1] += val - 1
                    next_next_tmp.append([nr, nc-1, val - 1])




    break