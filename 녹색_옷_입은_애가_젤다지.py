import sys
import heapq

dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(i=0,j=0):
    dist[i][j] = field[i][j]
    heap = []
    heapq.heappush(heap, (field[i][j], i, j))

    while heap:
        distance, r, c = heapq.heappop(heap)
        #print(distance, r,c)
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + field[nr][nc]
                heapq.heappush(heap, (dist[nr][nc], nr, nc))
num_p = 1
while True:
    N = int(sys.stdin.readline())
    if not N :
        break
    field = []
    for _ in range(N):
        field.append(list(map(int, sys.stdin.readline().split())))
    dist = [[-1]*N for _ in range(N)]
    bfs()
    print('Problem {}: '.format(num_p) + str(dist[N-1][N-1]))
    num_p += 1
