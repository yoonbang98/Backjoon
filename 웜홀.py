import sys
TC = int(sys.stdin.readline())
def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if distance[cur] + cost < distance[next] :
                distance[next] = distance[cur] + cost
                if i == N-1 :
                    return True
    return False


for _ in range(TC):
    answer = 'NO'
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S,E,-T))


    distance = [1e9] * (N + 1)
    if bellman_ford(1):
        answer = 'YES'
    print(answer)
