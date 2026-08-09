def solution(depth, money, excavate):
    n = len(depth)

    # dp[i][j]: i번째부터 j번째 열 사이에 보물이 있을 때 드는 최소 확정 비용
    # opt[i][j]: 그때 파야 할 최적의 열 인덱스
    dp = [[0] * (n + 1) for _ in range(n + 2)]
    opt = [[0] * (n + 1) for _ in range(n + 2)]

    # 길이를 1부터 n까지 늘려가며 DP 채우기
    for length in range(1, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            if i == j:
                dp[i][j] = depth[i-1]
                opt[i][j] = i
                continue

            res = float('inf')
            best_k = i
            for k in range(i, j + 1):
                # k를 팠을 때 발생하는 비용 + (왼쪽 혹은 오른쪽 중 더 비싼 쪽의 비용)
                cost = depth[k-1] + max(dp[i][k-1], dp[k+1][j])
                if cost < res:
                    res = cost
                    best_k = k
            dp[i][j] = res
            opt[i][j] = best_k


    # 계산된 최적 지점(opt)을 바탕으로 탐색 수행
    left, right = 1, n
    while left <= right:
        mid = opt[left][right] # 단순 중간이 아닌, 비용 최적화된 지점 선택
        result = excavate(mid)

        if result == 0:
            return mid
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1