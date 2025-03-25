import sys

R, C, M = map(int, sys.stdin.readline().split())
field = [[[] for _ in range(C)] for _ in range(R)]
dir = [[], [-1,0],[1,0],[0,1],[0,-1]]
for _ in range(M):
    r,c,s,d,z = map(int, sys.stdin.readline().split())
    field[r-1][c-1].append((s,d,z))
fisher_c = 0

answer = 0
while fisher_c != C:
    for r in range(R):
        if field[r][fisher_c]:
            answer += field[r][fisher_c][0][2]
            field[r][fisher_c] = []
            break
    new_field = [[[] for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if field[r][c]:
                s,d,z = field[r][c][0]
                cur_r, cur_c = r,c
                if d <= 2:
                    fast_s = s%(2*R-2)
                    cnt = 0
                    while cnt != fast_s:
                        nr, nc = cur_r + dir[d][0], cur_c + dir[d][1]
                        if 0 <= nr < R and 0 <= nc < C:
                            cur_r, cur_c = nr,nc
                            cnt += 1
                        else:
                            if d == 1:
                                d = 2
                            else:
                                d = 1
                    if new_field[cur_r][cur_c]:
                        _,_, zz = new_field[cur_r][cur_c][0]
                        if zz < z :
                            new_field[cur_r][cur_c][0] = (s,d,z)
                    else:
                        new_field[cur_r][cur_c].append((s,d,z))
                elif d > 2:
                    fast_s = s%(2*C-2)
                    cnt = 0
                    while cnt != fast_s:
                        nr, nc = cur_r + dir[d][0], cur_c + dir[d][1]
                        if 0 <= nr < R and 0 <= nc < C:
                            cur_r, cur_c = nr, nc
                            cnt += 1
                        else:
                            if d == 3:
                                d = 4
                            else:
                                d = 3
                    if new_field[cur_r][cur_c]:
                        _, _, zz = new_field[cur_r][cur_c][0]
                        if zz < z:
                            new_field[cur_r][cur_c][0] = (s, d, z)
                    else:
                        new_field[cur_r][cur_c].append((s, d, z))
    field = new_field
    fisher_c += 1
print(answer)