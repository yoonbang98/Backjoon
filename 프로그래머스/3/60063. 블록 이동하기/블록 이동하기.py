import heapq
from math import inf 

dir = [(1,0),(0,1),(-1,0),(0,-1)]
def solution(board):
    N = len(board)
    dist = [[[inf]*(N+1) for _ in range(N+1)] for _ in range(2)] 
    dist[0][1][2] = 0
    
    heap = []
    heapq.heappush(heap, [0, 0, 1,1, 1,2])#거리, 상태(0:가로, 1:세로), r1, c1, r2, c2
    
    while heap:
        d, state, r1, c1, r2, c2 = heapq.heappop(heap)
        for dr, dc in dir:
            nr1, nc1, nr2, nc2 = r1 + dr, c1 + dc, r2 + dr, c2 + dc

            if nr1 <= 0 or nr1 > N or nc1 <= 0 or nc1 > N or nr2 <= 0 or nr2 > N or nc2 <= 0 or nc2 > N : continue
            if board[nr1-1][nc1-1] or board[nr2-1][nc2-1]: continue

            if dist[state][nr2][nc2] > d + 1:
                heapq.heappush(heap, [d + 1, state, nr1, nc1, nr2, nc2])
                dist[state][nr2][nc2] = d+1
        if not state: #가로 -> 세로
            if 0 < r1 - 1 <= N and 0 < c1 + 1 <= N:
                if not board[r1-2][c1-1] and not board[r1-2][c1]:
                    if dist[1][r1][c1] > d + 1:
                        heapq.heappush(heap, [d+1 , 1, r1 -1, c1, r1, c1])
                        dist[1][r1][c1] = d + 1
                    if dist[1][r1][c1+1] > d + 1:
                        heapq.heappush(heap, [d+1 , 1, r1 -1, c1+1, r1, c1+1])
                        dist[1][r1][c1+1] = d + 1
            if 0 < r1 + 1 <= N and 0 < c1 + 1 <= N:
                if not board[r1][c1-1] and not board[r1][c1]:
                    if dist[1][r1+1][c1] > d + 1:
                        heapq.heappush(heap, [d+1 , 1, r1 , c1, r1+1, c1])
                        dist[1][r1+1][c1] = d + 1
                    if dist[1][r1+1][c1+1] > d + 1:
                        heapq.heappush(heap, [d+1 , 1, r1, c1+1, r1+1, c1+1])
                        dist[1][r1+1][c1+1] = d + 1
        else: #세로 -> 가로
            if 0 < c1 - 1 <= N and 0 < r1 + 1 <= N:
                if not board[r1-1][c1-2] and not board[r1][c1-2]:
                    if dist[0][r1][c1] > d + 1:
                        heapq.heappush(heap, [d+1 , 0, r1, c1-1, r1, c1])
                        dist[0][r1][c1] = d + 1
                    if dist[0][r1+1][c1] > d + 1:
                        heapq.heappush(heap, [d+1 , 0, r1 + 1, c1-1, r1+1, c1])
                        dist[0][r1+1][c1] = d + 1
            if 0 < c1 + 1 <= N and 0 < r1 + 1 <= N:
                if not board[r1-1][c1] and not board[r1][c1]:
                    if dist[0][r1][c1+1] > d + 1:
                        heapq.heappush(heap, [d+1 , 0, r1 , c1, r1, c1+1])
                        dist[0][r1][c1+1] = d + 1
                    if dist[0][r1+1][c1+1] > d + 1:
                        heapq.heappush(heap, [d+1 , 0, r1+1, c1, r1+1, c1+1])
                        dist[0][r1+1][c1+1] = d + 1
    #print(dist)
    answer = 0
    return min(dist[0][N][N], dist[1][N][N])