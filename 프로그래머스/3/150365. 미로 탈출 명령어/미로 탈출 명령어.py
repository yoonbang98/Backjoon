import heapq
dir = [[1,0, 'd'],[0,-1, 'l'],[0,1, 'r'],[-1,0,'u']] #dlru
def bfs(sr, sc, dst_r, dst_c, field, k):
    heap = []
    heapq.heappush(heap, [0,'', sr, sc]) #거리, route, 현재위치
    while heap:
        dist, route, cur_r, cur_c = heapq.heappop(heap)

        if field[cur_r][cur_c] == 'E' and -1*dist == k:
            return route
        for dr, dc, d in dir :
            if 0 <= cur_r + dr < len(field) and 0 <= cur_c + dc < len(field[0]) and -1*dist < k:
                nr, nc = cur_r + dr, cur_c + dc
                next_dist = abs(dst_r- nr) + abs(dst_c - nc)
                if next_dist > k + dist - 1 or (next_dist-(k+dist-1))%2 == 1: 
                    continue
                heapq.heappush(heap, [dist-1, route + d, nr, nc])  
def solution(n, m, x, y, r, c, k):
    field = [[0]*m for _ in range(n)]
    field[x-1][y-1] = 'S'
    field[r-1][c-1] = 'E'

    min_dist = abs(x-r) + abs(y-c)
    if min_dist > k or abs(min_dist-k)%2 == 1:
        return 'impossible'
    route = bfs(x-1, y-1, r-1, c-1, field, k)
    return route