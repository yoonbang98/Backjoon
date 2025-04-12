import sys

input = sys.stdin.readline
L, N, Q = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(L)]
field_knight = [[0]*L for _ in range(L)]
alive = [True]*(N+1)
damage = [0]*(N+1)
kngiht = [[]]
for n in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    for i in range(r, r+h):
        for j in range(c, c+w):
            field_knight[i][j] = n
    kngiht.append([r,c,h,w,k])
dir = [(-1,0),(0,1),(1,0),(0,-1)]
def move_knight(i, d):
    kr, kc, kh, kw, k = kngiht[i]
    pushed = []
    for r in range(kr, kr + kh):
        for c in range(kc, kc + kw):
            nr, nc = r + dir[d][0], c + dir[d][1]
            if 0 > nr or L <= nr or 0 > nc or L <= nc : return []
            if field[nr][nc] == 2 : return []
            if field_knight[nr][nc] and field_knight[nr][nc] != field_knight[r][c]:
                pushed.append(field_knight[nr][nc])
    if not pushed:
        return [i]
    prev_pushed = list(set(pushed))[:]
    while True:
        nxt_pushed = []
        for n in prev_pushed:
            kr, kc, kh, kw, k = kngiht[n]
            for r in range(kr, kr + kh):
                for c in range(kc, kc + kw):
                    nr, nc = r + dir[d][0], c + dir[d][1]
                    if 0 > nr or L <= nr or 0 > nc or L <= nc : return []
                    if field[nr][nc] == 2 : return []
                    if field_knight[nr][nc] and field_knight[nr][nc] != field_knight[r][c]:
                        nxt_pushed.append(field_knight[nr][nc])
                        pushed.append(field_knight[nr][nc])
        if not nxt_pushed:
            return [i] + list(set(pushed))
        prev_pushed = nxt_pushed[:]

command = []
for _ in range(Q):
    i, d = map(int, input().split())
    command.append([i,d])
for i, d in command:
    if alive[i]:
        move_list = move_knight(i, d)
        if not move_list : continue
        new_knight_field = [[0]*L for _ in range(L)]
        for idx, k_info in enumerate(kngiht):
            if idx == 0 : continue
            kr, kc, kh, kw, k = k_info
            if idx in move_list:
                cnt = 0
                nr, nc = kr + dir[d][0], kc + dir[d][1]
                for r in range(nr, nr + kh):
                    for c in range(nc, nc + kw):
                        new_knight_field[r][c] = idx
                        if field[r][c] == 1:
                            cnt += 1
                kngiht[idx] = [nr, nc, kh, kw, k]
                if idx != i:
                    k -= cnt
                    if k <= 0:
                        alive[idx] = False
                        for r in range(nr, nr + kh):
                            for c in range(nc, nc + kw):
                                new_knight_field[r][c] = 0
                    else:
                        damage[idx] += cnt
                        kngiht[idx][4] = k
            else :
                for r in range(kr, kr + kh):
                    for c in range(kc, kc + kw):
                        new_knight_field[r][c] = idx
        field_knight = new_knight_field
answer = 0
for n in range(1, N+1):
    if alive[n]:
        answer += damage[n]
print(answer)