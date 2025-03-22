import heapq
import sys
input = sys.stdin.readline

N = int(input())
leftHeap = []
rightHeap = []
for i in range(N):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])