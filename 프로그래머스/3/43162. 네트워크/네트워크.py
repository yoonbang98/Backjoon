from collections import deque
def bfs(start, visited, computers):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        for idx, edge in enumerate(computers[cur]):
            if idx == cur : continue
            if edge == 1 and not visited[idx]:
                queue.append(idx)
                visited[idx] = True
    return visited
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for start in range(n):
        if not visited[start]:
            answer += 1
            visited = bfs(start, visited, computers)
    
    return answer