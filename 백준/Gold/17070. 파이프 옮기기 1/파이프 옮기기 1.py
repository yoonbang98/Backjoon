N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(3)] #가로 세로 대각
dp[0][1][2] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        if j <= 2: continue
        if not field[i-1][j-1]:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        if i >= 2 and j >= 3:
            if not field[i-1][j-1] and not field[i-2][j-1] and not field[i-1][j-2]:
                dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
answer = dp[0][N][N] + dp[1][N][N] + dp[2][N][N]

print(answer)