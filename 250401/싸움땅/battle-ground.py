import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
field_gun = [[[] for _ in range(N)] for _ in range(N)]
field_warrior = [[[] for _ in range(N)] for _ in range(N)]
dir = [(-1,0),(0,1),(1,0),(0,-1)]#상우하좌
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        field_gun[i][j].append(row[j])
for m in range(M):
    r, c, d, s = map(int, input().split())
    field_warrior[r-1][c-1] = [m, d, s, 0] #번호, 방향, 초기 능력치, 총

answer = [0]*M
for _ in range(K):
    new_warrior = []
    for m in range(M):
        flag = False
        for r in range(N):
            for c in range(N):
                if field_warrior[r][c] and field_warrior[r][c][0] == m:
                    m, d, s, g = field_warrior[r][c]
                    field_warrior[r][c] = []
                    nr, nc = r + dir[d][0], c + dir[d][1]
                    if 0 > nr or N <= nr or 0 > nc or N <= nc :
                        d = (d+2)%4
                        nr, nc = r + dir[d][0], c + dir[d][1]
                    if not field_warrior[nr][nc] : #플레이어 없다면
                        cur_g = g
                        if max(field_gun[nr][nc]) > g:
                            cur_g = max(field_gun[nr][nc])
                            field_gun[nr][nc].remove(cur_g)
                            if not field_gun[nr][nc]:
                                field_gun[nr][nc] = [g]
                            else:
                                if g :
                                    field_gun[nr][nc].append(g)
                        field_warrior[nr][nc] = [m, d, s, cur_g]
                    else: #플레이어 있다면
                        m2, d2, s2, g2 = field_warrior[nr][nc]
                        score = abs(s + g - s2 - g2)
                        flag = False #m이 이길 경우 True
                        if s + g > s2 + g2:
                            flag = True
                        elif s2 + g2 > s + g:
                            pass
                        else:
                            if s > s2:
                                flag = True
                            else:
                                pass
                        if flag: #m이 이길 경우
                            answer[m] += score
                            if g2:
                                if not max(field_gun[nr][nc]):
                                    field_gun[nr][nc] = [g2]
                                else:
                                    field_gun[nr][nc].append(g2)
                            g2 = 0
                            while True:
                                nnr, nnc = nr + dir[d2][0], nc + dir[d2][1]
                                if 0 <= nnr < N and 0 <= nnc < N and not field_warrior[nnr][nnc]:
                                    if max(field_gun[nnr][nnc]):
                                        g2 = max(field_gun[nnr][nnc])
                                        field_gun[nnr][nnc].remove(g2)
                                        if not field_gun[nnr][nnc]:
                                            field_gun[nnr][nnc] = [0]

                                    field_warrior[nnr][nnc] = [m2, d2, s2, g2]

                                    break
                                else:
                                    d2 += 1
                            cur_g = g
                            if max(field_gun[nr][nc]) > g:
                                cur_g = max(field_gun[nr][nc])
                                field_gun[nr][nc].remove(cur_g)
                                if not field_gun[nr][nc]:
                                    field_gun[nr][nc] = [g]
                                else:
                                    if g :
                                        field_gun[nr][nc].append(g)
                            field_warrior[nr][nc] = [m, d, s, cur_g]
                        else : #m이 질 경우
                            answer[m2] += score
                            if g:
                                if not max(field_gun[nr][nc]):
                                    field_gun[nr][nc] = [g]
                                else:
                                    field_gun[nr][nc].append(g)
                            g = 0
                            while True:
                                nnr, nnc = nr + dir[d][0], nc + dir[d][1]
                                if 0 <= nnr < N and 0 <= nnc < N and not field_warrior[nnr][nnc]:
                                    if max(field_gun[nnr][nnc]):
                                        g = max(field_gun[nnr][nnc])
                                        field_gun[nnr][nnc].remove(g)
                                        if not field_gun[nnr][nnc]:
                                            field_gun[nnr][nnc] = [0]
                                    field_warrior[nnr][nnc] = [m, d, s, g]
                                    break
                                else:
                                    d += 1
                            cur_g = g2
                            if max(field_gun[nr][nc]) > g2:
                                cur_g = max(field_gun[nr][nc])
                                field_gun[nr][nc].remove(cur_g)
                                if not field_gun[nr][nc]:
                                    field_gun[nr][nc] = [g2]
                                else:
                                    if g2 :
                                        field_gun[nr][nc].append(g2)
                            field_warrior[nr][nc] = [m2, d2, s2, cur_g]
                    flag = True
                    break
            if flag :
                break
print(*answer)