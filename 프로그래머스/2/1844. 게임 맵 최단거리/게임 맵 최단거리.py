from collections import deque

dir = [(1,0),(-1,0),(0,1),(0,-1)]
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append([0,0])
    dist = [[-1]*m for _ in range(n)]
    dist[0][0] = 1
    
    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in dir:
            nr, nc = dr + cur_r, dc + cur_c
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if not maps[nr][nc] : continue
            if dist[nr][nc] == -1:
                queue.append([nr, nc])
                dist[nr][nc] = dist[cur_r][cur_c] + 1
    return dist[n-1][m-1]