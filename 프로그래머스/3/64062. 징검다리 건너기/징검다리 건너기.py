def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone - mid > 0:
                cnt = 0
            else :
                cnt += 1
            if cnt >= k:
                break
        if cnt >= k: #값을 줄여야함
            right = mid - 1
        else : 
            left = mid + 1

    return left