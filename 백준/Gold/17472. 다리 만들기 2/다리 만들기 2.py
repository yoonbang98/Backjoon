from collections import deque
from math import inf
N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]

island_num = 1
new_field = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if field[i][j] and not visited[i][j]:
            queue = deque()
            queue.append([i,j])
            visited[i][j] = True
            while queue:
                r, c = queue.popleft()
                new_field[r][c] = island_num
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and field[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append([nr,nc])
            island_num += 1
island_num -= 1

adj_mat = [[inf]*(island_num+1) for _ in range(island_num+1)]
for r in range(N):
    for c in range(M):
        if new_field[r][c]:
            for dr, dc in dir:
                sr, sc = r + dr, c + dc
                if 0 <= sr < N and 0 <= sc < M and not new_field[sr][sc]:
                    while True:
                        nr, nc = sr + dr, sc + dc
                        if 0 > nr or N <= nr or 0 > nc or M <= nc : break
                        if new_field[nr][nc]:
                            dist = abs(nr-r) + abs(nc-c) - 1
                            if dist > 1:
                                adj_mat[new_field[nr][nc]][new_field[r][c]] =  min(dist, adj_mat[new_field[nr][nc]][new_field[r][c]])
                                adj_mat[new_field[r][c]][new_field[nr][nc]] =  min(dist, adj_mat[new_field[r][c]][new_field[nr][nc]])
                            break
                        sr, sc = nr, nc
edges = []
for src in range(1, island_num+1):
    for dst in range(src+1, island_num+1):
        if adj_mat[src][dst] != inf:
            edges.append([adj_mat[src][dst], src, dst])
edges.sort()
parent = [i for i in range(island_num + 1)]
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
answer = 0
edge_cnt = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a,b)
        answer += cost
        edge_cnt += 1
if edge_cnt == island_num - 1:
    print(answer)
else:
    print(-1)