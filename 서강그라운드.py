import sys

n,m,r = map(int, sys.stdin.readline().split())
item_list = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l
for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

answer = 0
for start in range(1, n+1):
    tmp = item_list[start]
    dist_list = graph[start]
    for i, d in enumerate(dist_list):
        if i == start or d == 1e9 : continue
        else :
            if d <= m:
                tmp += item_list[i]
    answer = max(answer, tmp)
print(answer)