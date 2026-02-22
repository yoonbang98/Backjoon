import sys
import heapq

N = int(sys.stdin.readline())
heap = []

first = list(map(int, sys.stdin.readline().split()))
for num in first:
    heapq.heappush(heap, num)
for _ in range(N-1):
    num_list = list(map(int, sys.stdin.readline().split()))
    for num in num_list:
        if heap[0] < num:
            heapq.heappush(heap, num)
            heapq.heappop(heap)
print(heap[0])