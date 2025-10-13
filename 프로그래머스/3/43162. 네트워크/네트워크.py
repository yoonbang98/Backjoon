from collections import deque
def bfs(src, visited, graph):
    queue = deque()
    queue.append(src)
    visited[src] = True
    while queue:
        cur = queue.popleft()
        for nei in graph[cur]:
            if not visited[nei]:
                queue.append(nei)
                visited[nei] = True
    return visited
def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            if computers[i][j]:
                graph[i].append(j)
                graph[j].append(i)
    answer = 0
    visited = [False]*n
    for src in range(n):
        if not visited[src]:
            answer += 1
            visited = bfs(src, visited, graph)
    return answer