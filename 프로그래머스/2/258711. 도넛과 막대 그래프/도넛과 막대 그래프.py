from collections import deque
def solution(edges):
    N = 0
    answer = []
    for src, dst in edges:
        N = max(N, src, dst)
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1
    max_idx, max_num = 0, 0
    for idx, nei_list in enumerate(graph):
        if not idx : continue
        if len(nei_list) >= max_num and not indegree[idx]:
            max_num = len(nei_list)
            max_idx = idx
    answer.append(max_idx)
    answer.extend([0,0,0])
    visited = [False]*(N+1)
    for start in graph[max_idx]:
        queue = deque()
        queue.append(start)
        visited[start] = True
        num_edge, num_node = 0, 0
        while queue:
            cur = queue.popleft()
            num_edge += len(graph[cur])
            num_node += 1
            for nei in graph[cur]:
                if not visited[nei]:
                    queue.append(nei)
                    visited[nei] = True
        if num_edge == num_node:
            answer[1] += 1
        elif num_edge == num_node - 1:
            answer[2] += 1
        else:
            answer[3] += 1
    return answer