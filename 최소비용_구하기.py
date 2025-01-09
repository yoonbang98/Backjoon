import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dist = [1e9]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst, cost = map(int, sys.stdin.readline().split())
    graph[src].append((dst,cost))
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    dist[start] = 0
    while q:
        distance , node = heapq.heappop(q)
        if dist[node] < distance:
            continue
        for nei in graph[node]:
            cost = dist[node] + nei[1]
            if cost < dist[nei[0]]:
                dist[nei[0]] = cost
                heapq.heappush(q, (cost, nei[0]))
start, finish = map(int, sys.stdin.readline().split())

dijkstra(start)
print(dist[finish])
