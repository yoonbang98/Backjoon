def solution(n, times):
    times.sort()
    left, right = 0, times[0]*n
    while left <= right:
        mid = (left + right)//2
        cnt = 0
        for t in times:
            cnt += mid//t
        #print(cnt, mid)
        if cnt >= n: #사람 수가 많으면 -> 시간 줄이기
            right = mid - 1
        else:
            left = mid + 1    
    return left