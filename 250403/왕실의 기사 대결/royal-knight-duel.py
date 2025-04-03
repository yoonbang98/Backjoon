import sys
input = sys.stdin.readline
L, N, Q = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(L)]
knight = []
field_knight = [[0]*L for _ in range(L)]
alive = [True]*N
damage = [0]*N
for n in range(1,N+1):
    r,c,h,w,k = map(int, input().split())
    r -= 1
    c -= 1
    knight.append([r,c,h,w,k])
    for i in range(r, r+h):
        for j in range(c, c+ w):
            field_knight[i][j] = -n
def move(num,d,field_knight, knight):
    result = [num]
    r,c,h,w,k = knight[num]
    nxt_knight = []
    for i in range(r, r+ h):
        for j in range(c,c+w):
            nr, nc = i + dir[d][0], j+dir[d][1]
            if 0 <= nr < L and 0 <= nc < L and field[nr][nc] != 2:
                if field_knight[nr][nc] and field_knight[nr][nc] != -(num+1):
                    nxt_knight.append(-field_knight[nr][nc]-1)
            else:
                return []
    result += nxt_knight
    while len(nxt_knight) != 0:
        nxt_knight_tmp = []
        for n in nxt_knight:
            r,c,h,w,k = knight[n]
            for i in range(r, r+ h):
                for j in range(c,c+w):
                    nr, nc = i + dir[d][0], j+dir[d][1]
                    if 0 <= nr < L and 0 <= nr < L and field[nr][nc] != 2:
                        if field_knight[nr][nc] and field_knight[nr][nc] != -(n+1):
                            nxt_knight_tmp.append(-field_knight[nr][nc]-1)
                    else:
                        return []
        nxt_knight = nxt_knight_tmp
        result += nxt_knight
    return result
dir = [(-1,0),(0,1),(1,0),(0,-1)]#상우하좌
for _ in range(Q):
    i, d = map(int, input().split())

    if alive[i-1]:
        result = move(i-1, d,field_knight, knight)
        if not result:
            continue
        else:
            for n in result:
                r,c,h,w,k = knight[n]
                nr, nc = r + dir[d][0], c+dir[d][1]
                knight[n] = [nr,nc,h,w,k]
            new_field_knight = [[0]*L for _ in range(L)]
            for num, (r,c,h,w,k) in enumerate(knight):
                if num+1 != i:
                    cnt = 0
                    for ii in range(r, r+h):
                        for jj in range(c, c+ w):
                            if field[ii][jj] == 1:
                                cnt += 1
                    if k <= cnt:
                        alive[i-1] = False
                    else:
                        damage[i-1] += cnt
                        for ii in range(r, r+h):
                            for jj in range(c, c+ w):
                                new_field_knight[ii][jj] = -(num+1)
                        knight[num][4] = k-cnt
                else:
                    for ii in range(r, r+h):
                        for jj in range(c, c+ w):
                            new_field_knight[ii][jj] = -(num+1)
            field_knight = new_field_knight
answer = 0
for i in range(N):
    if alive[i]:
        answer += damage[i]
print(answer)
