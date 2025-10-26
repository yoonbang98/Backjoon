import heapq
from math import inf
def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n+1)]
    for src, dst, w in paths:
        graph[src].append([dst, w])
        graph[dst].append([src, w])
    
    is_summits = [0]*(n+1)
    for summit in summits:
        is_summits[summit] = True
    heap = []
    distance = [inf]*(n+1)
    for gate in gates:
        heapq.heappush(heap, [0, gate])
        distance[gate] = 0
        
    while heap:
        inten, cur = heapq.heappop(heap)
        
        if distance[cur] < inten or is_summits[cur]:
            continue
        for nei, weight in graph[cur]:
            new_inten = max(inten, weight)
            if distance[nei] > new_inten:
                heapq.heappush(heap, [new_inten, nei])
                distance[nei] = new_inten
    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result