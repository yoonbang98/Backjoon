from math import inf
def solution(n, s, a, b, fares):
    answer = 0
    dist = [[inf]*(n+1) for _ in range(n+1)]
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
    for i in range(n+1):
        dist[i][i] = 0
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    answer = dist[s][a] + dist[s][b]
    for mid in range(1, n+1):
        if mid == s : continue
        distance = dist[s][mid] + dist[mid][a] + dist[mid][b]

        if answer > distance:
            answer = distance
    return answer