import sys
import heapq
from collections import deque
input = sys.stdin.readline
N, M, F = map(int, input().split())

dir = [(0,1),(0,-1),(1,0),(-1,0)] #동서남북
wall_sr, wall_sc = -1, -1
field = [list(map(int, input().split())) for _ in range(N)]
exit_r, exit_c= -1, -1
final_exit_r, final_exit_c = -1, -1
for r in range(N):
    for c in range(N):
        if field[r][c] == 4 :
            final_exit_r, final_exit_c = r, c
        if field[r][c] == 3 :
            if(wall_sr, wall_sc) == (-1,-1):
                wall_sr, wall_sc = r, c
            flag = False
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if not field[nr][nc]:
                    exit_r, exit_c = nr, nc
                    flag = True
                    break
mountain = [[-1]*3*M for _ in range(3*M)]
m_sr, m_sc = M, M
for i in range(5):
    m_tmp = [list(map(int, input().split())) for _ in range(M)]
    if i == 0: #동
        m_tmp = list(map(list, zip(*m_tmp)))[::-1]
        for idx, row in enumerate(m_tmp):
            mountain[M + idx][2*M:] = row[:]
    elif i == 1: #서
        m_tmp = list(map(list, zip(*m_tmp[::-1])))
        for idx, row in enumerate(m_tmp):
            mountain[M + idx][:M] = row[:]
    elif i == 2: #남
        for idx, row in enumerate(m_tmp):
            mountain[2*M + idx][M:2*M]= row[:]
    elif i == 3: #북
        for _ in range(2):
            m_tmp = list(map(list, zip(*m_tmp)))[::-1]
        for idx, row in enumerate(m_tmp):
            mountain[idx][M:2*M]= row[:]
    else : #위
        for idx, row in enumerate(m_tmp):
            for idx2 in range(M):
                if row[idx2] == 2:
                    m_sr += idx
                    m_sc += idx2
            mountain[M+idx][M:2*M]= row[:]
fire = []
for _ in range(F):
    r, c, d, v = map(int, input().split())
    field[r][c] = -1
    fire.append([r,c,d,v])

r_diff, c_diff = exit_r - wall_sr, exit_c - wall_sc
if M + r_diff <= M -1 or M + r_diff >= 2*M:
    if M + r_diff <= M -1:
        m_dst_r, m_dst_c = 0, M + c_diff
    else:
        m_dst_r, m_dst_c = 3*M-1, M + c_diff
elif M + c_diff <= M -1 or M + c_diff >= 2*M:
    if M + c_diff <= M -1:
        m_dst_r, m_dst_c = M + r_diff, 0
    else:
        m_dst_r, m_dst_c = M + r_diff, 3*M-1
def down_mountain(mountain, m_sr, m_sc, m_dst_r, m_dst_c):
    dist = [[-1]*3*M for _ in range(3*M)]
    heap = []
    heapq.heappush(heap, [0, m_sr, m_sc])
    dist[m_sr][m_sc] = 0
    while heap:
        cur_dist, r,c = heapq.heappop(heap)
        if (r, c) == (m_dst_r, m_dst_c) :
            return cur_dist
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 > nr or nr >= 3*M or 0 > nc or nc >= 3*M: continue
            if not mountain[nr][nc] and dist[nr][nc] == -1:
                dist[nr][nc] = cur_dist + 1
                heapq.heappush(heap, [cur_dist + 1, nr, nc])
            if mountain[nr][nc] == -1:
                if 0 <= nr < M and 0 <= nc < M:
                    nr, nc = c, r
                elif nr >= 2*M and 0 <= nc < M:
                    nr, nc = -c + 3*M-1, -r+ 3*M-1
                elif 0 <= nr < M and nc >= 2*M:
                    nr, nc = -c + 3*M-1, -r+ 3*M-1
                else:
                    nr, nc = c, r
                if dist[nr][nc] == -1:
                    dist[nr][nc] = cur_dist + 1
                    heapq.heappush(heap, [cur_dist + 1, nr, nc])
    return -1
def fire_spread(t, field, fire):
    new_fire = []
    if not fire:
        return field, fire
    for r,c,d,v in fire:
        if t%v == 0:
            nr, nc = r + dir[d][0], c + dir[d][1]
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            if not field[nr][nc]:
                field[nr][nc] = -1
                new_fire.append([nr,nc,d,v])
        else:
            new_fire.append([r,c,d,v])
    return field, new_fire
t = 0
down_t = down_mountain(mountain, m_sr, m_sc, m_dst_r, m_dst_c)
if down_t == -1:
    print(-1)
else:
    for _ in range(down_t+1):
        t += 1
        field, fire = fire_spread(t, field, fire)
    if field[exit_r][exit_c] == -1:
        print(-1)
    else:
        dist = [[-1]*N for _ in range(N)]
        queue = deque()
        queue.append([t, exit_r, exit_c])
        dist[exit_r][exit_c] = t

        flag = False
        while True:
            t += 1
            field, fire = fire_spread(t, field, fire)
            nxt_loc = deque()
            while queue:
                cur_dist, r, c = queue.popleft()
                if field[r][c] == -1 : continue
                if (r, c) == (final_exit_r, final_exit_c):
                    flag = True
                    break
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
                    if not field[nr][nc] and dist[nr][nc] == -1:
                        nxt_loc.append([cur_dist+1, nr, nc])
                        dist[nr][nc] = cur_dist + 1
                    if field[nr][nc] == 4 and dist[nr][nc] == -1:
                        nxt_loc.append([cur_dist+1, nr, nc])
                        dist[nr][nc] = cur_dist + 1
            if flag :
                break
            if not nxt_loc:
                break
            queue = nxt_loc
        print(dist[final_exit_r][final_exit_c])