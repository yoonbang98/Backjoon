import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    order_tmp = list(map(int, sys.stdin.readline().split()))
    N_tmp = order_tmp[0]
    order_tmp = order_tmp[1:]
    for i in range(N_tmp-1):
        for j in range(i+1,N_tmp):
            src, dst = order_tmp[i], order_tmp[j]
            if dst not in graph[src]:
                graph[src].append(dst)
                indegree[dst] += 1
def topological_sort():
    result = []
    queue = deque()
    for n in range(1, N+1):
        if not indegree[n]:
            queue.append(n)
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for nei in graph[cur]:
            indegree[nei] -= 1
            if not indegree[nei]:
                queue.append(nei)
    return result
result = topological_sort()
if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)
