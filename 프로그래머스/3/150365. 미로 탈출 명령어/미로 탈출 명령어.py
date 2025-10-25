import heapq

dir = [[1,0, 'd'],[0,1, 'r'], [-1,0, 'u'], [0,-1, 'l']]        
            
def solution(n, m, x, y, r, c, k):
    answer = ''
    heap = []
    heapq.heappush(heap, [0, '', x, y])
    min_dist = abs(x-r) + abs(y-c)
    if min_dist > k or abs(min_dist-k)%2 == 1:
        return 'impossible'
    while heap:
        num, result, cur_r, cur_c = heapq.heappop(heap)
        if (abs(cur_r - r) + abs(cur_c - c))% 2 != (k - len(result))%2 : continue
        if len(result) >= k:
            if (cur_r, cur_c) == (r, c):
                return result
            continue
        for dr, dc, direction in dir:
            nr, nc = cur_r + dr, cur_c + dc
            if 0 >= nr or nr > n or 0 >= nc or nc > m: continue
            next_dist = abs(r- nr) + abs(c - nc)
            if next_dist > k + num - 1 or (next_dist-(k+num-1))%2 == 1: 
                continue

            heapq.heappush(heap, [num - 1, result + direction, nr, nc])
    return "impossible"