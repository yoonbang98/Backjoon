import sys
from collections import defaultdict
N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
num_dict = defaultdict(int)
num_dict[num_list[left]] = 1
max_key, max_value = num_list[left], 1
answer = 0
while right < N:
    if max_value <= K:
        answer = max(answer, right - left + 1)
        right += 1
        if right == N :
            break
        num_dict[num_list[right]] += 1
        if num_dict[num_list[right]] > max_value:
            max_value = num_dict[num_list[right]]
            max_key = num_list[right]
    else:
        num_dict[num_list[left]] -= 1
        if num_list[left] == max_key:
            max_value -= 1
        left += 1

print(answer)
