
answer = 0
def dfs(info, graph, visited, sheep, wolf, cur):
    global answer
    if sheep > answer:
        answer = sheep
    #print(cur, sheep ,wolf)
    for i in range(len(info)):
        if visited[i]:
            for nei in graph[i]:
                if not visited[nei]:
                    if not info[nei]:
                        visited[nei] = True
                        dfs(info, graph, visited, sheep + 1 , wolf, nei)
                        visited[nei] = False
                    elif info[nei] and sheep > wolf + 1:
                        visited[nei] = True
                        dfs(info, graph, visited, sheep , wolf + 1, nei)
                        visited[nei] = False
    return
def solution(info, edges):
    N = len(info)
    graph = [[] for _ in range(N)]
    visited = [False]*(N)
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    
    visited[0] = True
    dfs(info, graph, visited, 1, 0, 0)
            
    return answer