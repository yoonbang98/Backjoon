    
def solution(info, edges):
    answer = 1
    N = len(info)
    graph = [[] for _ in range(N)]

    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    
    def dfs(sheep, visited, wolf):
        nonlocal answer
        if sheep <= wolf:
            answer = max(answer, sheep)
            return
        answer = max(answer, sheep)
        for n in range(N):
            if visited[n]:
                for nei in graph[n]:
                    if not visited[nei] and info[nei]: #늑대
                        visited[nei] = True
                        dfs(sheep, visited, wolf + 1)
                        visited[nei] = False
                    elif not visited[nei] and not info[nei] : #양
                        visited[nei] = True
                        dfs(sheep + 1, visited, wolf)
                        visited[nei] = False
        return
    visited = [False]*N
    visited[0] = True
    dfs(1, visited, 0)
    
    return answer