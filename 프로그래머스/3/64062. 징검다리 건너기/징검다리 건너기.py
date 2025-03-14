def solution(stones, k):
    left, right = 1, 1e9
    while left <= right:
        mid = (left + right)//2
        cnt = 0
        flag = False
        for stone in stones:
            if mid <= stone: #밟을 수 있는 경우
                cnt = 0
            else : # 밟을 수 없는 경우
                cnt += 1
                if cnt >= k:
                    flag = True
                    break
        if flag : #건너지 못하는 경우, mid를 줄여야함
            right = mid - 1
        else:
            left = mid + 1   
                
    return min(left, right)