import sys
from collections import deque

N, M, energy = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
driver_r, driver_c = map(int, sys.stdin.readline().split())
driver_r -= 1
driver_c -= 1
src_list = []
dst_list = []

dir = [(0,1),(1,0),(-1,0),(0,-1)]
def bfs(i,j):
    global visited
    global dist
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    while queue:
        r,c = queue.popleft()
        for drow, dcol in dir:
            nr = drow + r
            nc = dcol + c
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and field[nr][nc] == 0:
                queue.append((nr,nc))
                visited[nr][nc] = 1
                dist[nr][nc] = dist[r][c] + 1

for _ in range(M):
    src_r, src_c, dst_r, dst_c = map(int, sys.stdin.readline().split())
    src_list.append((src_r-1, src_c-1))
    dst_list.append((dst_r-1,dst_c-1))

cannot_reach = False
energy_low = False
while len(src_list) != 0:
    visited = [[False]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    bfs(driver_r, driver_c)

    src_tmp = []
    for src_r, src_c in src_list:
        if visited[src_r][src_c]:
            src_tmp.append((dist[src_r][src_c], src_r, src_c))
        else :
            cannot_reach = True
            break
    if cannot_reach:
        break
    sorted_src_tmp = sorted(src_tmp, key=lambda x: (x[0], x[1], x[2]))
    distance, next_src_r, next_src_c = sorted_src_tmp[0]

    if energy >= distance:
        energy -= distance
    else:
        energy_low = True
        break

    driver_r, driver_c = next_src_r, next_src_c
    del_idx = src_list.index((next_src_r, next_src_c))
    next_dst_r, next_dst_c = dst_list[del_idx]

    del src_list[del_idx]
    del dst_list[del_idx]

    visited = [[False]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    bfs(driver_r, driver_c)

    if visited[next_dst_r][next_dst_c]:
        distance = dist[next_dst_r][next_dst_c]
    else:
        cannot_reach = True
        break
    if energy >= distance:
        energy += distance
    else:
        energy_low = True
        break
    driver_r, driver_c = next_dst_r, next_dst_c

if not cannot_reach and not energy_low:
    print(energy)
else:
    print(-1)

