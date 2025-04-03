import sys
input = sys.stdin.readline
L, N, Q = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(L)]
field_knight = [[0]*L for _ in range(L)]
knight = [[]]
alive = [True]*(N+1)
damage = [0]*(N+1)
for n in range(1,N+1):
    r,c,h,w,k = map(int, input().split())
    r -= 1
    c -= 1
    knight.append([r,c,h,w,k])
    for i in range(r, r+h):
        for j in range(c, c+ w):
            field_knight[i][j] = -n

def move(num,d):
    result = [num] #움직여야하는 기사 번호
    r,c,h,w,k = knight[num]

    nxt_knight = []
    for i in range(r, r+ h):
        for j in range(c,c+w):
            nr, nc = i + dir[d][0], j+dir[d][1]
            if 0 <= nr < L and 0 <= nc < L and field[nr][nc] != 2:
                if field_knight[nr][nc] and field_knight[nr][nc] != -(num):
                    nxt_knight.append(-field_knight[nr][nc])
            else:
                return []
    if not nxt_knight:
        return result
    nxt_knight = list(set(nxt_knight))
    result += nxt_knight
    while len(nxt_knight) != 0:
        nxt_knight_tmp = []
        for n in nxt_knight:
            r,c,h,w,k = knight[n]
            for i in range(r, r+ h):
                for j in range(c,c+w):
                    nr, nc = i + dir[d][0], j+dir[d][1]
                    if 0 <= nr < L and 0 <= nc < L and field[nr][nc] != 2:
                        if field_knight[nr][nc] and field_knight[nr][nc] != -(n):
                            if -field_knight[nr][nc] not in result:
                                nxt_knight_tmp.append(-field_knight[nr][nc])
                    else:
                        return []
        nxt_knight = nxt_knight_tmp
        nxt_knight = list(set(nxt_knight))
        result += nxt_knight
    return result
dir = [(-1,0),(0,1),(1,0),(0,-1)]#상우하좌
for _ in range(Q):
    i, d = map(int, input().split())
    if alive[i]:
        result = move(i, d)
        if not result: #이동 못하는 경우
            continue
        else:
            new_field_knight = [[0]*L for _ in range(L)]
            for n in result:
                r,c,h,w,k = knight[n]
                nr, nc = r + dir[d][0], c+dir[d][1]
                if n != i: #연쇄적 이동 기사
                    cnt = 0
                    for ii in range(nr, nr+h):
                        for jj in range(nc, nc+ w):
                            if field[ii][jj] == 1:
                                cnt += 1
                    if k <= cnt:
                        alive[n] = False
                    else:
                        damage[n] += cnt
                        for ii in range(nr, nr+h):
                            for jj in range(nc, nc+ w):
                                new_field_knight[ii][jj] = -(n)
                        knight[n][4] = k-cnt
                else: # 명령을 받은 기사
                    for ii in range(nr, nr+h):
                        for jj in range(nc, nc+ w):
                            new_field_knight[ii][jj] = -(n)
                knight[n] = [nr,nc,h,w,k] #좌상단

            for num in range(1, N+1):
                if alive[num] and num not in result:
                    r,c,h,w,k = knight[num]
                    for ii in range(r, r+h):
                        for jj in range(c, c+ w):
                            new_field_knight[ii][jj] = -(num)
            field_knight = new_field_knight

answer = 0
for i in range(1,N+1):
    if alive[i]:
        answer += damage[i]
print(answer)

