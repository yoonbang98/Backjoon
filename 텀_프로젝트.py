import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    nei_list = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n+1)]
    for idx, nei in enumerate(nei_list):
        graph[idx+1].append(nei)
    answer = 0
    global_visited = [False]*(n+1)
    for start in range(1,n+1):
        if global_visited[start]: continue
        visited = [False]*(n+1)
        queue = deque()
        queue.append(start)
        tmp = []
        tmp.append(start)
        while queue:
            cur = queue.popleft()
            if not visited[graph[cur][0]]:
                queue.append(graph[cur][0])
                visited[graph[cur][0]] = True
                tmp.append(graph[cur][0])
        if not visited[start]:
            answer += 1
        else:
            for t in tmp:
                global_visited[t] = True
    print(answer)