import sys
field = []

N = int(sys.stdin.readline())
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
dp = [[[0]*N for _ in range(N)] for _ in range(3)] # 가로, 세로, 대각선
first_row = field[0]
for idx, v in enumerate(first_row):
    if v:
        break
    dp[0][0][idx] = 1
dp[0][0][0] = 0

for r in range(1,N):
    for c in range(1, N):
        if not field[r][c]:
            dp[0][r][c] = dp[2][r][c-1] + dp[0][r][c-1]
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
            if not field[r-1][c] and not field[r][c-1]:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])