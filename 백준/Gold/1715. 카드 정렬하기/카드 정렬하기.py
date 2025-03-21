import heapq
import sys
input = sys.stdin.readline

N = int(input())
card = [int(input()) for _ in range(N)]
heapq.heapify(card)
answer = 0
while card:
    cur = heapq.heappop(card)
    if not card:
        break
    cur2 = heapq.heappop(card)
    answer += (cur + cur2)
    heapq.heappush(card, cur + cur2)
print(answer)