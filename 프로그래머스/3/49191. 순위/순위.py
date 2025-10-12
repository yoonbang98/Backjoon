from collections import deque
from math import inf
def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    for src, dst in results:
        graph[dst][src] = 1
        graph[src][dst] = -1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j or graph[i][j]:
                    continue
                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
    for idx, row in enumerate(graph):
        if idx > 0:
            if row[1:].count(0) == 1:
                answer += 1

    return answer