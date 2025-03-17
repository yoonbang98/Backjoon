import sys
sys.setrecursionlimit(10**7)
N, M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(i , j ,result, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, result)
        return
    for dr, dc in dir:
        nr, nc = i + dr, j + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr,nc,result + field[nr][nc], cnt + 1)
            visited[nr][nc] = False
    return

answer = 0
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,field[i][j],1)
        visited[i][j] = 0
        if j+2 < M: # 가로로 놓을 수 있으면
            if i-1 >= 0: # 위
                answer = max(answer, field[i][j] + field[i][j+1] + field[i][j+2] + field[i-1][j+1])
            if i+1 < N : #아래
                answer = max(answer, field[i][j] + field[i][j+1] + field[i][j+2] + field[i+1][j+1])
        if i+2 < N : #세로로 놓을 수 있으면
            if j-1 >= 0: # 왼쪽
                answer = max(answer, field[i][j] + field[i+1][j] + field[i+2][j] + field[i+1][j-1])
            if j+1 < M : #오른쪽
                answer = max(answer, field[i][j] + field[i+1][j] + field[i+2][j] + field[i+1][j+1])
print(answer)