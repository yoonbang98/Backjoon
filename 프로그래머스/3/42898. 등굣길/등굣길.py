def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dir = [[1,0],[0,1]]#아래 오른쪽
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puddles: continue
            cnt = 0
            for dr, dc in dir:
                nr, nc = i + dr, j + dc
                if 0 <= nr < n and 0 <= nc < m and [nc + 1, nr + 1] not in puddles:
                    dp[nr][nc] += dp[i][j]
            # print(i,j)
            # print(dp)
    return dp[n-1][m-1]% 1000000007