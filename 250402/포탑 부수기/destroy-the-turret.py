import heapq

N, M, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
field_attack = [[0]*M for _ in range(N)]

t = 1
def find_attacker(field):
    min_value, max_value = 5001, -1
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                min_value = min(min_value, field[i][j])
                max_value = max(max_value, field[i][j])
    min_cand = []
    max_cand = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == min_value:
                min_cand.append([min_value, field_attack[i][j], i+j, j,i])
            if field[i][j] == max_value:
                max_cand.append([max_value, field_attack[i][j], i+j, j,i])
    min_cand.sort(key = lambda x : (x[0],-x[1],-x[2],-x[3]))
    max_cand.sort(key = lambda x : (-x[0],x[1],x[2],x[3]))

    return min_cand[0][4], min_cand[0][3], max_cand[0][4], max_cand[0][3]
l_dir = [(0,1),(1,0),(0,-1),(-1,0)]#우하좌상
def l_attack(src_r, src_c, dst_r, dst_c):
    dist = [[-1]*M for _ in range(N)]
    heap = []
    heapq.heappush(heap, [0, [], src_r, src_c])
    dist[src_r][src_c] = 0
    while heap:
        cur_dist, route, cur_r, cur_c = heapq.heappop(heap)
        if (cur_r, cur_c) == (dst_r, dst_c) :
            return route
        for idx, (dr, dc) in enumerate(l_dir):
            nr, nc = (cur_r + dr)%N, (cur_c + dc)%M
            if dist[nr][nc] == -1 and field[nr][nc]:
                dist[nr][nc] = cur_dist + 1
                heapq.heappush(heap, [cur_dist+1, route + [idx], nr, nc])
    return []
p_dir = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
def p_attack(field, field_war, src_r, src_c, dst_r, dst_c):
    field[dst_r][dst_c] = max(0, field[dst_r][dst_c] - field[src_r][src_c])
    field_war[dst_r][dst_c] = True
    for dr, dc in p_dir:
        nr, nc = (dst_r + dr)%N, (dst_c+dc)%M
        if field[nr][nc] and (nr, nc) != (src_r, src_c):
            field_war[nr][nc] = True
            field[nr][nc] = max(0, field[nr][nc] - int(field[src_r][src_c]//2))
    return field, field_war
for _ in range(K):
    field_war = [[False]*M for _ in range(N)]
    src_r, src_c, dst_r, dst_c = find_attacker(field)
    field[src_r][src_c] += (N+M)
    field_attack[src_r][src_c] = t
    field_war[src_r][src_c] = True

    route = l_attack(src_r, src_c, dst_r, dst_c)
    if route : #레이저 공격 가능
        r, c = src_r, src_c
        for d in route:
            r = (r + l_dir[d][0])%N
            c = (c+ l_dir[d][1])%M
            field_war[r][c] = True
            if (r,c) == (dst_r, dst_c):
                field[r][c] = max(0, field[r][c] - field[src_r][src_c])
            else:
                field[r][c] = max(0, field[r][c] - int(field[src_r][src_c]//2))
    else: #포탄 공격
        field, field_war = p_attack(field, field_war, src_r, src_c, dst_r, dst_c)
    cnt = 0
    for i in range(N): #종료 조건 확인
        for j in range(M):
            if field[i][j] :
                cnt += 1
    if cnt == 1:
        break
    for i in range(N): #포탑 정비
        for j in range(M):
            if field[i][j] and not field_war[i][j]:
                field[i][j] += 1
answer = 0
for row in field:
    answer = max(answer, max(row))
print(answer)
