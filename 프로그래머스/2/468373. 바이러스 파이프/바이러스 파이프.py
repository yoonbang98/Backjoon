import copy
from collections import deque
answer = 0

def dfs(visited, depth, edges, k, graph):
    global answer
    if depth == k:
        answer = max(answer, sum(visited))
        return
    for t in range(1, 4):
        new_visited = visited.copy()
        queue = deque()
        for src, dst, num in edges:
            if num == t:
                if visited[src] and not visited[dst]:
                    new_visited[dst] = True
                    queue.append(dst)
                if visited[dst] and not visited[src]:
                    new_visited[src] = True
                    queue.append(src)
        while queue:
            cur = queue.popleft()
            for nei, edge_t in graph[cur]:
                if edge_t == t and not new_visited[nei]:
                    new_visited[nei] = True
                    queue.append(nei)
        dfs(new_visited, depth + 1, edges, k, graph)
    return 
                    
def solution(n, infection, edges, k):
    
    graph = [[] for _ in range(n+1)]
    for src, dst, t in edges:
        graph[src].append([dst, t])
        graph[dst].append([src, t])
    visited = [False]*(n+1)
    visited[infection] = True
    dfs(visited, 0, edges, k, graph)
    
    return answer