import sys

N = int(sys.stdin.readline())
dp = []
for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N):
    for j in range(0, i+1):
        if j == 0: #왼쪽 모서리
            dp[i][0] += dp[i-1][0]
        elif j == i: #오른쪽 모서리
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])
    #print(dp)

print(max(dp[N-1]))

