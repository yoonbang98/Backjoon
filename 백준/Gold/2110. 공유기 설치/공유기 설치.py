import sys
N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

answer = 0
def binary_search(data,C):
    start = 1
    end = data[-1] - data[0]
    global answer
    while start <= end:
        mid = (start + end) // 2
        current = data[0]
        cnt = 1

        for i in range(1, len(data)):
            if data[i] >= current + mid:
                cnt += 1
                current = data[i]

        if cnt >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
binary_search(house,C)
print(answer)