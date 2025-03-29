from collections import deque
import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(int, input().split())
taxi_r -= 1
taxi_c -= 1
target = []
for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    sr -= 1
    sc -= 1
    er -= 1
    ec -= 1
    target.append([sr, sc, er, ec])
dir = [(1,0),(0,1),(-1,0),(0,-1)]
target_visited = []
def bfs(field, taxi_r, taxi_c, target):
    dist = [[-1]*N for _ in range(N)]
    queue = deque()
    queue.append([taxi_r, taxi_c, 0])
    dist[taxi_r][taxi_c] = 0

    while queue:
        r, c, cur_dist = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            if dist[nr][nc] == -1 and not field[nr][nc]:
                dist[nr][nc] = cur_dist + 1
                queue.append([nr,nc, cur_dist + 1])
    next_cand = []
    for sr, sc, er, ec in target:
        if [sr, sc] in target_visited: continue
        next_cand.append([dist[sr][sc], sr, sc, er, ec])
    if not next_cand:
        return []
    next_cand.sort(key = lambda x : (x[0],x[1],x[2]))
    return next_cand[0]
def bfs2(field, sr, sc, er, ec):
    dist = [[-1]*N for _ in range(N)]
    queue = deque()
    queue.append([sr, sc, 0])
    dist[sr][sc] = 0

    while queue:
        r, c, cur_dist = queue.popleft()
        if r == er and c == ec:
            return cur_dist
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            if dist[nr][nc] == -1 and not field[nr][nc]:
                dist[nr][nc] = cur_dist + 1
                queue.append([nr,nc, cur_dist + 1])
    return -1
while True:
    next_loc = bfs(field, taxi_r, taxi_c, target)
    if next_loc[0] > fuel or not next_loc or next_loc[0] == -1:
        fuel = -1
        break
    fuel -= next_loc[0]
    taxi_r, taxi_c = next_loc[1], next_loc[2]
    target_visited.append([taxi_r, taxi_c])
    dist_end = bfs2(field, taxi_r, taxi_c, next_loc[3], next_loc[4])
    if dist_end > fuel or dist_end == -1:
        fuel = -1
        break
    fuel += dist_end
    taxi_r, taxi_c = next_loc[3], next_loc[4]
    if len(target) == len(target_visited):
        break
print(fuel)
