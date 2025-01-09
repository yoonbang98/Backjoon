import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1)
if N <= 2:
    if N == 1:
        print(0)
    else:
        print(3)
else:
    dp[2] = 3
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
    print(dp[N])

