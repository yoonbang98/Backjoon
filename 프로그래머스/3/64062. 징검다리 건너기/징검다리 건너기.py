def solution(stones, k):
    left, right = 1, 1e9
    
    while left <= right:
        mid = (left + right) // 2
        flag = False
        cnt = 0 
        for stone in stones:
            if stone >= mid:
                cnt = 0
            else:
                cnt += 1
                if cnt >= k:
                    flag = True
                    break
        if flag:
            right = mid - 1
        else:
            left = mid + 1
    print(left, right)
    answer = 0
    return min(left, right)