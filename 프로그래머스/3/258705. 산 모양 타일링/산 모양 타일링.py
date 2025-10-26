def solution(n, tops):
    dp_square = [0]*(n+1)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n):
        if tops[i] : #위에 삼각형이 있을 때
            dp_square[i+1] = (dp_square[i] + dp[i])%10007
            dp[i+1] = (3*dp[i] + 2*dp_square[i])%10007
        else: #위에 삼각형이 없을 때
            dp_square[i+1] = (dp_square[i] + dp[i])%10007
            dp[i+1] = (2*dp[i] + dp_square[i])%10007

    return sum(dp)%10007