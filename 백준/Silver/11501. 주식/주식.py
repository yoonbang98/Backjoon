import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    price_list = list(map(int, sys.stdin.readline().split()))
    answer = 0

    max_price = 0
    for i in range(N-1, -1, -1):
        if price_list[i] > max_price:
            max_price = price_list[i]
        else:
            answer += max_price - price_list[i]
    print(answer)