import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    A,B,C = map(int, sys.stdin.readline().split())
    graph[A].append([C,B])
    graph[B].append([C,A])

src, dst = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
cost= [0]*(N+1)
heap = []
heapq.heappush(heap, [-1000000000, src])

while heap:
    w, cur = heapq.heappop(heap)
    cost[cur] = max(-w, cost[cur])
    if cur == dst:
        break
    if visited[cur] == 1:
        continue
    visited[cur] = 1
    for c, nei in graph[cur]:
        if cost[nei] < min(cost[cur], c):
            cost[nei] = max(cost[nei], min(cost[cur], c))
            heapq.heappush(heap, [-cost[nei], nei])
print(cost[dst])
