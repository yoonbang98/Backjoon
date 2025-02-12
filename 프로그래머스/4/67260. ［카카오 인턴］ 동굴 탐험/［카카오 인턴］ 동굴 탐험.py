def solution(n, path, order):
    answer = True
    graph = [[] for _ in range(n+1)]
    for src, dst in path:
        graph[src].append(dst)
        graph[dst].append(src)
    orders = [0]*n
    for pre, nxt in order:
        orders[nxt] = pre
    visited = [0]*n
    queue = [0]
    num_visit = 0
    
    after = {}
    while queue :
        cur = queue.pop()
        if orders[cur] and not visited[orders[cur]]:
            after[orders[cur]] = cur
            continue
        visited[cur] = 1
        num_visit += 1
        
        for nei in graph[cur]:
            if not visited[nei]:
                queue.append(nei)
        if cur in after:
            queue.append(after[cur])

    return n == num_visit