def solution(n, times):
    left = 1
    right = max(times)*n
    answer = 0
    while left <= right:
        people = 0
        mid = (left+right)//2
        for time in times:
            people += mid//time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
    
    return answer