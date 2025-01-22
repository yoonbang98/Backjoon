


def solution(info, edges):
    def dfs(sheep, wolf):
        nonlocal answer
        if sheep == wolf :
            answer = max(answer, sheep)
            return 
        for n in range(N):
            if visited[n]:
                for nei in graph[n]:
                    if not visited[nei]:
                        if info[nei] == 0 : #양
                            visited[nei] = True
                            dfs(sheep + 1, wolf)
                            visited[nei] = False
                        else : #늑대
                            visited[nei] = True
                            dfs(sheep, wolf + 1)
                            visited[nei] = False
        answer = max(answer, sheep)
        return
    N = len(info)
    graph = [[] for _ in range(N)]
    visited = [False]*N
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    
    visited[0] = True
    answer = 1
    dfs(1,0)
    
    
    return answer