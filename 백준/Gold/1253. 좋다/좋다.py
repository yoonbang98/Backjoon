import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

answer = 0
for i in range(N):
    num_list_tmp = []
    for idx, num in enumerate(num_list):
        if i != idx :
            num_list_tmp.append(num)
        else:
            target = num
    left, right = 0, N-2
    while left < right:
        val = num_list_tmp[left] + num_list_tmp[right]
        if val < target:
            left += 1
        elif val > target:
            right -= 1
        else:
            answer += 1
            break
print(answer)