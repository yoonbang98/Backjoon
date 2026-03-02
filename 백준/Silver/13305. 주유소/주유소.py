import sys

N = int(sys.stdin.readline())
road_length = list(map(int, sys.stdin.readline().split()))
price_l = list(map(int, sys.stdin.readline().split()))

price_list = []
for i in range(N-1):
    price_list.append([price_l[i], i])
price_list.sort()
visited = [False]*(N+1)
answer = 0
for price, idx in price_list:
    d_tmp = 0
    for j in range(idx, N-1):
        if not visited[j + 1]:
            d_tmp += road_length[j]
            visited[j + 1] = True
    answer += price*d_tmp
print(answer)
