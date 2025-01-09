n = int(input())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))
answer = 1e9
for c in range(3):
    dp = [[-1]*3 for _ in range(n)]
    dp[0] = [1e9, 1e9, 1e9]
    dp[0][c] = a[0][c]
    for i in range(1, n):  # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + a[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + a[i][2]
    dp[n-1][c] = 1e9
    answer = min(answer, min(dp[n-1]))
print(answer)