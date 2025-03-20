import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()

left, right = 1, house[-1]
answer= 0
while left <= right:
    mid = (left+right)//2
    cnt = 1 #설치해야하는 공유기 수
    cur = house[0]

    for i in range(1, len(house)):
        if house[i] >= cur + mid:
            cur = house[i]
            cnt += 1
    if cnt >= C: #공유기 많음 -> 거리 증가
        answer = mid
        left = mid + 1
    else:
        right = mid -1
print(answer)