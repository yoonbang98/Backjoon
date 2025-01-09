import sys
N = int(sys.stdin.readline())

schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0 for i in range(N+1)]
for n in range(N): # 모든 day에 대하여 iteration
    date = schedule[n][0]
    price = schedule[n][1]
    for m in range(n+date, N+1): # m : day n에 상담을 했을 때, 상담이 가능한 모든 날짜
        if dp[m] < dp[n] + price:
            dp[m] = dp[n] + price

print(dp[-1])