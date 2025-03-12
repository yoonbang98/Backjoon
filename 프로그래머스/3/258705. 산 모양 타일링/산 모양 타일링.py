def solution(n, tops):
    dp = []
    for i in range(2*n + 1):
        dp.append([0]*3)
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(2*n+1):
        if not i :
            continue
        if i%2 == 1 : #윗변
            dp[i][1] = (dp[i-1][0]+dp[i-1][2])%10007 
            if tops[i//2]: #위에 놓여져 있는 경우
                dp[i][0] = (sum(dp[i-1]))%10007
                dp[i][2] = (dp[i-1][0]+dp[i-1][2])%10007
            else:
                dp[i][0] = (dp[i-1][0]+dp[i-1][2])%10007
                dp[i][2] = (dp[i-1][1])%10007
        else : #아랫변
            dp[i][0] = (dp[i-1][0]+dp[i-1][2])%10007 #작은 삼각형만 놓는 경우
            dp[i][1] = (dp[i-1][0]+dp[i-1][2])%10007
            dp[i][2] = (dp[i-1][1])%10007


    return (dp[-1][0] + dp[-1][2])%10007