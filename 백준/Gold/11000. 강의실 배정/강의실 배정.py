import heapq
import sys
input = sys.stdin.readline

N = int(input())
class_list = []
for _ in range(N):
    s, t = map(int, input().split())
    class_list.append([s,t])
class_list.sort(key = lambda x : (x[0], x[1]))

heap = [class_list[0][1]]

for i in range(1, N):
    if heap[0] <= class_list[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, class_list[i][1])
print(len(heap))
