import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

answer = 0
if sum(n_list) <= M :
    answer = max(n_list)
else:
    left, right = 1, max(n_list)
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for num in n_list:
            if mid <= num:
                tmp += mid
            else:
                tmp += num
        if tmp <= M: #아직 여유
            left = mid + 1
            answer = mid
        else :
            right = mid - 1
print(answer)
