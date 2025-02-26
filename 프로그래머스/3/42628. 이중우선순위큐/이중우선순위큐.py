import heapq
def solution(operations):
    heap = []
    for oper in operations:
        command, num = oper.split()
        if command == 'I':
            heapq.heappush(heap, int(num))
        else:
            if int(num) == -1: #최솟값 삭제
                if heap:
                    heapq.heappop(heap)

            else: #최댓값 삭제
                if heap:
                    heap.sort()
                    heap.pop()
    heap.sort()
    return [heap[-1], heap[0]] if heap else [0,0]