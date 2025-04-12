from collections import deque
dir = [(0,1),(0,-1),(1,0),(-1,0)] #동서남북
N, M, F = map(int, input().split())
field = []
exit_r, exit_c, m_exit_r, m_exit_c = -1, -1, -1, -1
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 4:
            exit_r, exit_c = i, j
    field.append(row)
flag = False
m_field_sr, m_field_sc = -1, -1
for i in range(N):
    for j in range(N):
        if field[i][j] == 3:
            if m_field_sr == -1:
                m_field_sr, m_field_sc = i, j
            for dr, dc in dir:
                nr, nc = i + dr, j + dc
                if not field[nr][nc]:
                    m_exit_r, m_exit_c = nr, nc
                    flag = True
                    break
        if flag:
            break
    if flag:
        break
field_mountain = [[-1]*3*M for _ in range(3*M)]
m_sr, m_sc = M, M
for i in range(5):
    tmp = [list(map(int, input().split())) for _ in range(M)]
    if i == 0: #동
        tmp = list(map(list, zip(*tmp)))[::-1]
        for idx, row in enumerate(tmp):
            field_mountain[M+idx][2*M:] = row
    elif i == 1: #서
        tmp = list(map(list, zip(*tmp[::-1])))
        for idx, row in enumerate(tmp):
            field_mountain[M+idx][:M] = row
    elif i == 2: #남
        for idx, row in enumerate(tmp):
            field_mountain[2*M+idx][M:2*M] = row
    elif i == 3: #북
        for _ in range(2):
            tmp = list(map(list, zip(*tmp[::-1])))
        for idx, row in enumerate(tmp):
            field_mountain[idx][M:2*M] = row
    else: #위
        for i in range(M):
            for j in range(M):
                if tmp[i][j] == 2:
                    m_sr += i
                    m_sc += j
        for idx, row in enumerate(tmp):
            field_mountain[M+idx][M:2*M] = row
r_diff, c_diff = m_exit_r - m_field_sr, m_exit_c - m_field_sc
m_er, m_ec = m_sr + r_diff, m_sc + c_diff
if m_er >= 2*M:
    m_er = 3*M - 1
elif m_er < M:
    m_er = 0
elif m_ec >= 2*M:
    m_ec = 3*M - 1
elif m_ec < M :
    m_ec = 0
def down_mountain(m_sr, m_sc, m_er, m_ec):
    dist = [[-1]*3*M for _ in range(3*M)]
    dist[m_sr][m_sc] = 0
    queue = deque()
    queue.append([m_sr, m_sc])
    while queue:
        cur_r, cur_c = queue.popleft()
        if (cur_r, cur_c) == (m_er, m_ec):
            return dist[m_er][m_ec]
        for dr, dc in dir:
            nr, nc = cur_r + dr, cur_c + dc
            if nr < 0 or nr >= 3*M or nc < 0 or nc >= 3*M: continue
            if dist[nr][nc] == -1 and not field_mountain[nr][nc]:
                dist[nr][nc] = dist[cur_r][cur_c] + 1
                queue.append([nr,nc])
            elif field_mountain[nr][nc] == -1:
                if (0 <= nr < M and 2*M <= nc) or (2*M <= nr and 0 <= nc < M):
                    new_r, new_c = -cur_c + 3*M - 1, -cur_r + 3*M - 1
                elif (0 <= nr < M and 0 <= nc < M) or (2*M <= nr and 2*M <= nc):
                    new_r, new_c = cur_c, cur_r
                if dist[new_r][new_c] == -1 and not field_mountain[new_r][new_c]:
                    dist[new_r][new_c] = dist[cur_r][cur_c] + 1
                    queue.append([new_r,new_c])
    return -1
def fire_spread(field, fire_list):
    new_fire_list = []
    if not fire_list:
        return field, []
    for r,c,d,v in fire_list:
        if t%v == 0:
            nr, nc = r + dir[d][0], c + dir[d][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if field[nr][nc] : continue
            field[nr][nc] = -1
            new_fire_list.append([nr,nc,d,v])
        else:
            new_fire_list.append([r,c,d,v])
    return field, new_fire_list
fire_list = []
for _ in range(F):
    r,c,d,v = map(int, input().split())
    fire_list.append([r,c,d,v])
    field[r][c] = -1
t = 0
down_time = down_mountain(m_sr, m_sc, m_er, m_ec)
if down_time == -1:
    print(-1)
else:
    for _ in range(down_time + 1):
        t += 1
        field, fire_list = fire_spread(field, fire_list)
    if field[m_exit_r][m_exit_c] == -1:
        print(-1)
    else:
        dist = [[-1]*N for _ in range(N)]
        dist[m_exit_r][m_exit_c] = t
        queue = deque()
        queue.append([m_exit_r, m_exit_c])
        arrive = False
        while True:
            t += 1
            field, fire_list = fire_spread(field, fire_list)
            nxt_loc = deque()
            while queue:
                r, c = queue.popleft()
                if (r, c) == (exit_r, exit_c):
                    arrive = True
                    break
                if field[r][c] == -1 : continue
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                    if not field[nr][nc] and dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        nxt_loc.append([nr,nc])
                    if field[nr][nc] == 4 and dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        nxt_loc.append([nr,nc])
            queue = nxt_loc
            if not queue or arrive:
                break
        print(dist[exit_r][exit_c])