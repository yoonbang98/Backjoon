import heapq
from math import inf
dir = [(-1,0), (1,0), (0,-1), (0,1)] #상하좌우
def solution(board):
    N = len(board)
    dist = [[[inf]*N for _ in range(N)] for _ in range(4)] 
    for i in range(4):
        dist[i][0][0] = 0
    heap = []
    heapq.heappush(heap, [0, 0, 0, -1]) #cost, r, c, 이전 방향
    
    while heap:
        cost, r, c, prev_d_idx = heapq.heappop(heap)
        for d_idx, (dr, dc) in enumerate(dir):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
                if prev_d_idx == -1 or prev_d_idx == d_idx:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                if dist[d_idx][nr][nc] >= new_cost:
                    dist[d_idx][nr][nc] = new_cost
                    if (nr, nc) != (N-1, N-1):
                        heapq.heappush(heap, [new_cost, nr, nc, d_idx])
    answer = inf
    for i in range(4):
        answer = min(answer, dist[i][N-1][N-1])
    return answer