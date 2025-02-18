from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for src, dst in edge:
        graph[src].append(dst)
        graph[dst].append(src)
    dist = [-1]*(n+1)
    dist[1] = 0
    queue = deque()
    queue.append([1, 0])
    while queue:
        cur, d = queue.popleft()
        for nei in graph[cur]:
            if dist[nei] == -1:
                dist[nei] = d + 1
                queue.append([nei, d+1])
            elif dist[nei] > d + 1:
                dist[nei] = d + 1
                queue.append([nei, d+1])
    return dist.count(max(dist))