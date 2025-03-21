def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    left, right = 0, distance
    answer = 0
    while left <= right:
        mid = (left + right)//2
        cnt = 0
        cur = 0
        for rock in rocks:
            if mid > rock - cur: #기준 거리 미만 -> 지워야함
                cnt += 1
            else:
                cur = rock
        if cnt > n: #너무 많이 제거함 -> 기준 거리 줄이기
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer