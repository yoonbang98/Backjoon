import heapq
def solution(places):
    answer = []
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    for place in places:
        flag = True
        for i, row in enumerate(place):
            for j, seat in enumerate(row):
                if seat == 'P':
                    visited = [[-1]*5 for _ in range(5)]
                    visited[i][j] = 0
                    heap = []
                    heapq.heappush(heap, [0, i, j])
                    while heap:
                        d, r, c = heapq.heappop(heap)
                        if place[r][c] == 'P':
                            if 0 < d <= 2:
                                flag = False
                                break
                        for dr, dc in dir:
                            nr, nc = r + dr, c + dc
                            if 0 > nr or 5 <= nr or 0 > nc or 5 <= nc: continue
                            if place[nr][nc] == 'X': continue
                            if visited[nr][nc] == -1:
                                heapq.heappush(heap, [d + 1, nr, nc])
                                visited[nr][nc] = d + 1
                                
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer