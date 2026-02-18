import sys
from math import inf

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
left, right = 0, N-1

answer = inf
left_a, right_a = num_list[left], num_list[right]

while left < right:
    val = num_list[left] + num_list[right]
    if val < 0:
        if answer > abs(val):
            answer = abs(val)
            left_a, right_a = num_list[left], num_list[right]
        left += 1
    elif val > 0 :
        if answer > abs(val):
            answer = abs(val)
            left_a, right_a = num_list[left], num_list[right]
        right -= 1
    else:
        left_a, right_a = num_list[left], num_list[right]
        break
print(left_a, right_a)