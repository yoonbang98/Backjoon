from math import inf
def solution(n, s, a, b, fares):

    answer = 0
    graph = [[inf]*(n+1) for _ in range(n+1)]
    for src, dst, fare in fares:
        graph[src][dst] = fare
        graph[dst][src] = fare
    for i in range(n+1):
        graph[i][i] = 0
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    threshold = graph[s][a] + graph[s][b]
    print(threshold)
    answer = threshold
    for mid in range(1, n+1):
        if mid == s : continue
        distance = graph[s][mid] + graph[mid][a] + graph[mid][b]

        if answer > distance:
            answer = distance
    return answer