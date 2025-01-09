import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
cost = [0]*(N+1)

for n in range(1,N+1):
    row = list(map(int, sys.stdin.readline().split()))
    cost[n] = row[0]
    if len(row) == 2:
        continue
    for nei in row[1:-1]:
        graph[nei].append(n)
        indegree[n] += 1
def topology_sort():
    queue = deque()
    result = [0] * (N+1)
    for n in range(1, N+1):
        if not indegree[n]:
            queue.append(n)
    while queue:
        now = queue.popleft()
        result[now] += cost[now]
        for nei in graph[now]:
            indegree[nei] -= 1
            result[nei] = max(result[nei], result[now])
            if not indegree[nei]:
                queue.append(nei)
    return result
result = topology_sort()
for i in range(1, N + 1):
    print(result[i])