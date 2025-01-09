import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))

dir = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(i,j, num): #탐색하면서 섬의 번호 마킹
    global visited
    global field
    visited[i][j] = True
    field[i][j] = num
    queue = deque()
    queue.append((i,j))
    while queue:
        r, c = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and field[nr][nc]:
                field[nr][nc] = num
                visited[nr][nc] = True
                queue.append((nr,nc))
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else :
        parent[b] = a

visited = [[False] * M for _ in range(N)]
num = 1
for n in range(N):
    for m in range(M):
        if field[n][m] and not visited[n][m]:
            bfs(n,m,num)
            num += 1
num -= 1
graph = [[1e9]*(num+1) for _ in range(num+1)]
for n in range(N):
    for m in range(M):
        if field[n][m]: #섬이면
            for dr, dc in dir:
                nr, nc = n + dr, m + dc
                if 0 <= nr < N and 0 <= nc < M and not field[nr][nc]: # 바다면
                    while True:
                        nr += dr
                        nc += dc
                        if 0 <= nr < N and 0 <= nc < M:
                            if field[nr][nc] : # 섬이면
                                if field[nr][nc] != field[n][m]: #다른 섬이면
                                    dist = abs(nr-n) + abs(nc-m)-1
                                    if dist >= 2:
                                        graph[field[n][m]][field[nr][nc]] = min(graph[field[n][m]][field[nr][nc]],dist)
                                        graph[field[nr][nc]][field[n][m]] = min(graph[field[nr][nc]][field[n][m]], dist)
                                    break
                                else: # 같은 섬이면
                                    break
                        else: # 바깥으로 나갈 경우
                            break

Edge = []
for i in range(1,num+1):
    for j in range(i,num+1):
        if 2 <= graph[i][j] < 1e9:
            Edge.append((graph[i][j],i,j))
# print(Edge)
# print(field)
Edge.sort()
parent = [0]*(num+1)
for i in range(1, num+1):
    parent[i] = i
answer = 0
edge_num = 0
for edge in Edge:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        edge_num += 1
        union_parent(parent, a,b)
        answer += cost
if not answer or edge_num != (num-1):
    print(-1)
else :
    print(answer)