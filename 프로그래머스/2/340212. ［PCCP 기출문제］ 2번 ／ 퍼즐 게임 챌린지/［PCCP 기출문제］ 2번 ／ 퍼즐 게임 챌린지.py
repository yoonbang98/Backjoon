def solution(diffs, times, limit):
    n = len(diffs)
    left, right = 1, sum(diffs)
    anawer = 0
    while left <= right:
        mid = (left + right) // 2
        result = 0
        for i in range(n):
            diff, time_cur = diffs[i], times[i]
            if mid >= diff :
                result += time_cur
            else:
                if i > 0 :
                    result += (diff - mid) *(times[i-1] + time_cur) + time_cur
                else:
                    result += (diff - mid) *(time_cur) + time_cur
            # print(mid, i, result)
        if result > limit: #시간 초과, 레벨 올려야함
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    
    return answer