import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

answer = 0

dir = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(r, c, route):
    global answer
    if len(route) == 4:
        result = 0
        for rr, cc in route:
            result += field[rr][cc]
        answer = max(answer, result)
        return

    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and [nr, nc] not in route:
            route_next = route + [[nr, nc]]
            dfs(nr, nc, route_next)
    return
for sr in range(N):
    for sc in range(M):
        route = [[sr, sc]]
        dfs(sr, sc, route)
        if 1 <= sc < M -1 and 1 <= sr:
            tmp = field[sr][sc] + field[sr][sc-1] + field[sr][sc + 1] + field[sr-1][sc]
            answer = max(answer, tmp)
        if 1 <= sc < M -1 and sr < N - 1:
            tmp = field[sr][sc] + field[sr][sc-1] + field[sr][sc + 1] + field[sr+1][sc]
            answer = max(answer, tmp)
        if 1 <= sr < N -1 and 1 <= sc:
            tmp = field[sr][sc] + field[sr-1][sc] + field[sr+1][sc] + field[sr][sc-1]
            answer = max(answer, tmp)
        if 1 <= sr < N -1 and sc < M - 1:
            tmp = field[sr][sc] + field[sr-1][sc] + field[sr+1][sc] + field[sr][sc+1]
            answer = max(answer, tmp)
print(answer)