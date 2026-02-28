import sys

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]

dp = [1]*(N)

for i in range(1,N):
    for j in range(i):
        if num_list[j]<num_list[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(N - max(dp))
