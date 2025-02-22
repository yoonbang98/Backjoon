def solution(triangle):
    H = len(triangle)
    dp = [[] for _ in range(H)]
    dp[0] = [triangle[0][0]]
    for i, row in enumerate(triangle):
        if i == 0 : continue
        W = len(row)
        for idx, num in enumerate(row):
            if idx == 0 or idx == W-1:
                if idx == 0:
                    dp[i].append(dp[i-1][0] + triangle[i][idx])
                else:
                    dp[i].append(dp[i-1][idx-1]+ triangle[i][idx])
            else:
                dp[i].append(max(dp[i-1][idx-1]+ triangle[i][idx], dp[i-1][idx]+ triangle[i][idx]))
                    
    return max(dp[-1])