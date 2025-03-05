from math import inf
answer = inf
N, S = map(int, input().split())
num_list = list(map(int, input().split()))
start, end = 0, 0
sum_tmp = num_list[0]
while True:
    if sum_tmp < S:
        end += 1
        if end == N : break
        sum_tmp += num_list[end]
    else:
        sum_tmp -= num_list[start]
        answer = min(answer, end - start + 1)
        start += 1
print(answer if answer != inf else 0)
