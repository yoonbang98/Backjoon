import heapq
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for src, dst in edge:
        graph[src].append(dst)
        graph[dst].append(src)
    dist = [-1]*(n+1)
    heap = [[1, 0]]
    dist[1] = 0
    while heap:
        cur_node, cur_dist = heapq.heappop(heap)
        for nei in graph[cur_node]:
            if dist[nei] == -1 or dist[nei] > dist[cur_node] + 1:
                heapq.heappush(heap, [nei, cur_dist + 1])
                dist[nei] = dist[cur_node] + 1
    max_num = max(dist)
    for i, num in enumerate(dist):
        if i > 0 and max_num == num:
            answer += 1
    return answer