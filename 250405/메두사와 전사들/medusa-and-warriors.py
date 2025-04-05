import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
warrior = list(map(int, input().split()))
field_warrior = [[[] for _ in range(N)] for _ in range(N)]
idx = 0
for _ in range(M):
    wr, wc = warrior[idx], warrior[idx+1]
    field_warrior[wr][wc].append(1)
    idx += 2
field = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]#상하좌우
dir2 = [(0,-1),(0,1),(-1,0),(1,0)]#좌우상하

def move_medusa(mr, mc, er, ec):
    dist = [[-1]*N for _ in range(N)]
    heap = []
    heapq.heappush(heap, [0, [], mr, mc])
    dist[mr][mc] = 0
    while heap:
        cur_dist, route, r, c = heapq.heappop(heap)
        if (r, c) == (er, ec):
            return route
        for idx, (dr, dc) in enumerate(dir):
            nr, nc = r + dr, c + dc
            if 0 > nr or N <= nr or 0 > nc or N <= nc : continue
            if not field[nr][nc] and dist[nr][nc] == -1:
                dist[nr][nc] = cur_dist + 1
                heapq.heappush(heap, [cur_dist + 1, route + [idx], nr, nc])
    return -1
def medusa_sight(mr, mc):
    result = []
    for idx, (dr, dc) in enumerate(dir):
        initial_sight = [[0]*N for _ in range(N)]
        dark_sight = [[0]*N for _ in range(N)]
        final_sight = [[0]*N for _ in range(N)]
        if idx <= 1: #상하
            r, c = mr + dr, mc
            cnt = 1
            warrior_loc = []
            while 0 <= r < N:
                for j in range(c-cnt, c+cnt+1):
                    if 0 <= j < N:
                        initial_sight[r][j] = 1
                    if 0 <= j < N and field_warrior[r][j]:
                        warrior_loc.append([r,j])
                cnt += 1
                r += dr
            if warrior_loc:
                for wr, wc in warrior_loc:
                    if dark_sight[wr][wc]: continue #이미 시야 가려진 상태
                    r, c = wr + dr, wc
                    cnt = 1
                    while 0 <= r < N:
                        if mc == wc :
                            c_min, c_max = wc, wc
                        elif mc < wc:
                            c_min, c_max = wc, wc + cnt
                        else :
                            c_min, c_max = wc - cnt, wc
                        for j in range(c_min, c_max+1):
                            if 0 <= j < N:
                                dark_sight[r][j] = 1
                        cnt += 1
                        r += dr
            cnt = 0
            for i in range(N):
                for j in range(N):
                    if initial_sight[i][j] and not dark_sight[i][j]:
                        final_sight[i][j] = 1
                        cnt += len(field_warrior[i][j])
            result.append([cnt, idx, final_sight])

        else: #좌우
            r, c = mr, mc + dc
            cnt = 1
            warrior_loc = []
            while 0 <= c < N:
                for i in range(r-cnt, r+cnt+1):
                    if 0 <= i < N:
                        initial_sight[i][c] = 1
                    if 0 <= i < N and field_warrior[i][c]:
                        warrior_loc.append([i,c])
                cnt += 1
                c += dc
            if warrior_loc:
                for wr, wc in warrior_loc:
                    if dark_sight[wr][wc]: continue #이미 시야 가려진 상태
                    r, c = wr, wc + dc
                    cnt = 1
                    while 0 <= c < N:
                        if mr == wr :
                            r_min, r_max = wr, wr
                        elif mr < wr:
                            r_min, r_max = wr, wr + cnt
                        else :
                            r_min, r_max = wr - cnt, wr
                        for i in range(r_min, r_max+1):
                            if 0 <= i < N:
                                dark_sight[i][c] = 1
                        cnt += 1
                        c += dc
            cnt = 0
            for i in range(N):
                for j in range(N):
                    if initial_sight[i][j] and not dark_sight[i][j]:
                        final_sight[i][j] = 1
                        cnt += len(field_warrior[i][j])
            result.append([cnt, idx, final_sight])
    result.sort(key = lambda x : (-x[0] ,x[1]))
    return result[0][0], result[0][2]
def move_warrior(field_warrior, mr ,mc):
    dist_num, attack_num = 0, 0
    new_field_warrior = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if field_warrior[i][j] and not field_sight[i][j]: #돌이 되지 않은 전사
                cur_dist = abs(i-mr) + abs(j-mc)
                flag = False
                for idx, (dr, dc) in enumerate(dir):
                    nr, nc = i + dr, j + dc
                    if 0 > nr or N <= nr or 0 > nc or N <= nc : continue
                    nxt_dist = abs(nr-mr) + abs(nc-mc)
                    if cur_dist > nxt_dist and not field_sight[nr][nc]:
                        flag = True
                        break
                if not flag: #첫번째 이동 불가
                    new_field_warrior[i][j] += field_warrior[i][j]
                if flag : # 첫번째 이동 가능
                    dist_num += len(field_warrior[i][j])
                    if (nr, nc) == (mr, mc): #메두사 도달
                        attack_num += len(field_warrior[i][j])
                        continue
                    cur_dist = abs(nr-mr) + abs(nc-mc)
                    flag = False
                    for idx, (dr, dc) in enumerate(dir2):
                        nnr, nnc = nr + dr, nc + dc
                        if 0 > nnr or N <= nnr or 0 > nnc or N <= nnc : continue
                        nxt_dist = abs(nnr-mr) + abs(nnc-mc)
                        if cur_dist > nxt_dist and not field_sight[nnr][nnc]:
                            flag = True
                            break
                    if not flag: #두번째 이동 불가
                        new_field_warrior[nr][nc] += field_warrior[i][j]
                    if flag : # 두번째 이동 가능
                        dist_num += len(field_warrior[i][j])
                        if (nnr, nnc) == (mr, mc): #메두사 도달
                            attack_num += len(field_warrior[i][j])
                            continue
                        new_field_warrior[nnr][nnc] += field_warrior[i][j]

            elif field_warrior[i][j] and field_sight[i][j]: #돌이 된 전사
                new_field_warrior[i][j] += field_warrior[i][j]

    return dist_num, attack_num, new_field_warrior
mr, mc = sr, sc
route = move_medusa(mr, mc, er, ec)
if route == -1: #도달할 수 없는 경우
    print(-1)
else:
    for md in route[:-1]:
        mr += dir[md][0]
        mc += dir[md][1]
        field_warrior[mr][mc] = [] #메두사가 공격

        stone_num, field_sight = medusa_sight(mr, mc)
        dist_num, attack_num, field_warrior = move_warrior(field_warrior, mr, mc)
        print(dist_num, stone_num, attack_num)
    print(0)