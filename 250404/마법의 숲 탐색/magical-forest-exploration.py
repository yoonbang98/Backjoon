import sys
from collections import deque
input = sys.stdin.readline

R, C, K = map(int, input().split())
dir = [(-1,0),(0,1),(1,0),(0,-1)]

field = [[0]*C for _ in range(R+3)]
answer = 0
cnt = 1
def bfs(sr, sc):
    visited = [[False]*C for _ in range(R+3)]
    queue = deque()
    queue.append([sr, sc, field[sr][sc]])
    visited[sr][sc] = True
    result = sr
    while queue:
        r, c, num = queue.popleft()
        result = max(result, r)
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= (R+3) or nc < 0 or nc >= C: continue
            if not field[nr][nc] : continue
            if num < 0 : #현재 골렘 출구 -> 모두 이동 가능
                if not visited[nr][nc] :
                    queue.append([nr,nc,field[nr][nc]])
                    visited[nr][nc] = True
            else:
                if num == field[nr][nc] or num == -field[nr][nc]:
                    if not visited[nr][nc] :
                        queue.append([nr,nc,field[nr][nc]])
                        visited[nr][nc] = True
    return result

for _ in range(K):
    ci, di = map(int, input().split())
    ci -= 1
    sr, sc = 1, ci #정령 위치기준

    while True:
        if not field[sr+1][sc-1] and not field[sr+2][sc] and not field[sr+1][sc+1]:
            sr += 1
        elif sc >= 2 and not field[sr-1][sc-1] and not field[sr][sc-2] and not field[sr+1][sc-1] and not field[sr+1][sc-2] and not field[sr+2][sc-1]:
            sr += 1
            sc -= 1
            di = (di - 1)%4
        elif sc <= C-3 and not field[sr-1][sc+1] and not field[sr][sc+2] and not field[sr+1][sc+1] and not field[sr+1][sc+2] and not field[sr+2][sc+1]:
            sr += 1
            sc += 1
            di = (di + 1)%4
        else:
            break
        if sr >= R +1 : break
    exit_r, exit_c = sr + dir[di][0], sc + dir[di][1]
    field[sr][sc], field[sr+1][sc], field[sr-1][sc], field[sr][sc-1], field[sr][sc+1] = cnt, cnt, cnt, cnt, cnt
    field[exit_r][exit_c] = -cnt

    flag = False
    for i in range(3):
        for j in range(C):
            if field[i][j]:
                flag = True

    if flag :
        field = [[0]*C for _ in range(R+3)]
        cnt = 1
        continue
    cnt += 1
    result = bfs(sr,sc)
    answer += result - 2

print(answer)