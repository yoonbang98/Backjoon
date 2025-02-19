def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance
    #print(rocks)
    answer = 0
    while left <= right:
        mid = (left + right)//2
        #print(mid)
        #print(left, right)
        cnt = 0
        
        loc = 0
        for stone in rocks:
            dist = stone - loc
            #print(stone, loc, dist)
            if dist < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                loc = stone
        if cnt > n: #너무 많이 지운 경우 -> mid가 너무 높음
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
                    
    return answer