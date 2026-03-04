import sys

N, D, K, C = map(int, sys.stdin.readline().split())

num_list = [int(sys.stdin.readline()) for _ in range(N)]
num_list_tmp = num_list + num_list
answer = 0
for i in range(N):
    target = num_list_tmp[i:i+K]
    tmp = set(target)
    tmp.add(C)
    answer = max(answer, len(tmp))
print(answer)