def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance
    answer = 0
    while left <= right:
        mid = (left + right)//2
        
        cnt = 0
        loc = 0
        for stone in rocks:
            dist = stone - loc
            if dist < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                loc = stone
        #print(mid, cnt)
        if cnt > n: #너무 많이 지운 경우 -> mid가 너무 높음
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
                    
    return answer