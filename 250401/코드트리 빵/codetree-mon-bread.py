import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
field = []
base = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            base.append([i,j])
    field.append(row)

field_red = [[0]*N for _ in range(N)]
cu = []
arrive = [False]*M
for m in range(1,M+1):
    r, c = map(int, input().split())
    field[r-1][c-1] = -1*m
    cu.append([r-1, c-1])
dir = [(-1,0),(0,-1),(0,1),(1,0)] #상좌우하
def bfs(sr, sc):
    dist = [[-1]*N for _ in range(N)]
    queue = deque()
    queue.append([sr, sc, 0])
    dist[sr][sc] = 0

    while queue:
        r, c, d = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 > nr or N <= nr or 0 > nc or N <= nc : continue
            if dist[nr][nc] == -1 and not field_red[nr][nc]:
                dist[nr][nc] = d + 1
                queue.append([nr, nc, d+1])
    base_cand = []
    for br, bc in base:
        if dist[br][bc] != -1:
            base_cand.append([dist[br][bc], br, bc])
    base_cand.sort()
    return base_cand[0][1], base_cand[0][2]
def dijkstra(r,c,dst_r,dst_c):
    heap = []
    heapq.heappush(heap, [0, [-1], r, c]) #이동거리, 방향 리스트, 현재 위치
    dist = [[-1]*N for _ in range(N)]
    dist[r][c] = 0
    while heap:
        d, route, r, c = heapq.heappop(heap)
        if (r, c) == (dst_r, dst_c):
            return route
        for idx, (dr, dc) in enumerate(dir):
            nr, nc = r + dr, c + dc
            if 0 > nr or N <= nr or 0 > nc or N <= nc : continue
            if dist[nr][nc] == -1 and not field_red[nr][nc]:
                heapq.heappush(heap, [d+1, route + [idx], nr, nc])
                dist[nr][nc] = d + 1
def move(field_person, field_red):
    global arrive
    new_field_person = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if field_person[r][c]:
                for num in field_person[r][c]:
                    dst_r, dst_c = cu[num-1]
                    route = dijkstra(r,c,dst_r,dst_c)
                    nxt_r, nxt_c = r + dir[route[1]][0], c + dir[route[1]][1]
                    if (nxt_r, nxt_c) == (dst_r, dst_c):
                        arrive[num-1] = True
                    else:
                        new_field_person[nxt_r][nxt_c].append(num)
    for idx, flag in enumerate(arrive):
        if flag:
            dst_r, dst_c = cu[idx]
            field_red[dst_r][dst_c] = 1
    return new_field_person, field_red
field_person = [[[] for _ in range(N)] for _ in range(N)]
t = 1
while True:
    if t >= 2:
        field_person, field_red = move(field_person, field_red)
    if t <= M: #3번
        sr, sc = cu[t-1]
        r, c = bfs(sr, sc)
        field_person[r][c].append(t)
        field_red[r][c] = 1
    if arrive == [True]*M:
        break
    t += 1
print(t)