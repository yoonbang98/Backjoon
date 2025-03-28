import sys
input = sys.stdin.readline
N = int(input())
dir = [(0,1),(-1,0),(0,-1),(1,0)]
visited = [[False]*101 for _ in range(101)]
for _ in range(N):
    c, r, d, g = map(int, input().split())
    route = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(route)-1, -1, -1):
            tmp.append((route[i] + 1)%4)
        route += tmp
    visited[r][c] = True
    for d in route:
        r += dir[d][0]
        c += dir[d][1]
        visited[r][c] = True
answer = 0

for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            answer += 1
print(answer)