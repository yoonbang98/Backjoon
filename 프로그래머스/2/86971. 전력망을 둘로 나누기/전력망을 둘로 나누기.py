from collections import deque
def solution(n, wires):
    answer = 100000
    for del_idx in range(n-1):
        graph = [[] for _ in range(n+1)]
        for idx, (src, dst) in enumerate(wires):
            if del_idx == idx : continue
            graph[src].append(dst)
            graph[dst].append(src)
        visited = [False]*(n)
        start = 1
        queue = deque()
        queue.append(start)
        visited[start-1] = True
        while queue:
            cur = queue.popleft()
            for nei in graph[cur]:
                if not visited[nei-1]:
                    queue.append(nei)
                    visited[nei-1] = True

        cnt = 0
        for flag in visited:
            if flag : cnt += 1

        answer = min(answer, abs(cnt - n + cnt))
    return answer