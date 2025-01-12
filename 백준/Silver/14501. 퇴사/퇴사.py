import sys

N = int(sys.stdin.readline())
schedule = []
dp = [0] * (N+1)
for _ in range(N):
    T, P = map(int, sys.stdin.readline().split())
    schedule.append([T,P])

for i in range(N):
    for j in range(i+schedule[i][0], N+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])