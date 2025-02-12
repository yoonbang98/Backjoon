def dfs(graph, path, cur, visited):
    if len(path) == len(visited):
        return path
    print(path)
    for nei in graph[cur]:
        if not visited[nei]:
            visited[nei] = True
            dfs(graph, path + [nei], nei, visited)
            visited[nei] = False
    return [-1]

def solution(n, path, order):
    answer = True
    graph = [[] for _ in range(n+1)]
    for src, dst in path:
        graph[src].append(dst)
        graph[dst].append(src)
    print(graph)
    visited = [False]*(n)
    visited[0] = True
    path = dfs(graph, [0], 0, visited)
    print(path)
    return answer