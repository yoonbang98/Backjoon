from collections import deque

def solution(n, path, order):
    answer = False
    graph = [[] for _ in range(n)]
    for src, dst in path:
        graph[src].append(dst)
        graph[dst].append(src)
    not_yet = [False]*n
    for src, dst in order:
        not_yet[dst] = src
    visited = [False]*n
    visited[0] = True
    queue = deque()
    queue.append(0)
    after = {}
    num_visit = 0
    while queue:
        cur = queue.popleft()
        prev = not_yet[cur]
        if prev and not visited[prev]:
            after[prev] = cur
            continue
        num_visit += 1
        for nei in graph[cur]:
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)
        if cur in after:
            visited[after[cur]] = True
            queue.append(after[cur])
    if num_visit == n:
        answer = True
    return answer