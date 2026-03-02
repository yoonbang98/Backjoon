import sys

N = int(sys.stdin.readline())
road_length = list(map(int, sys.stdin.readline().split()))
price_l = list(map(int, sys.stdin.readline().split()))

answer = 0
min_value = 1e9

for cur in range(N-1):
    if cur == 0:
        answer += road_length[cur]*price_l[cur]
        min_value = min(min_value, price_l[cur])
    else:
        min_value = min(min_value, price_l[cur])
        answer += road_length[cur]*min_value
print(answer)