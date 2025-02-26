import heapq
def solution(jobs):
    N = len(jobs)
    time_table = [[0,0] for _ in range(N)]
    for idx, (si, li) in enumerate(jobs):
        time_table[idx][0] = si

    cnt = 0
    t1 = 0
    heap = []
    disk = []
    while True:
        for idx, (si, li) in enumerate(jobs):
            if si == t1:
                heapq.heappush(heap, [li, si, idx])
        if heap :
            if not disk: #대기 큐 있고 디스크 놀 때
                li,si,idx = heapq.heappop(heap)
                disk.append([li, si, idx])
            else : #대기 큐 있는데 디스크 차 있을 때
                disk[0][0] -= 1
                if disk[0][0] == 0:
                    cnt += 1
                    time_table[disk[0][2]][1] = t1
                    disk = []
                    li,si,idx = heapq.heappop(heap)
                    disk.append([li, si, idx])
        else: 
            if disk:
                disk[0][0] -= 1
                if disk[0][0] == 0:
                    cnt += 1
                    time_table[disk[0][2]][1] = t1
                    disk = []
        t1 += 1
        if cnt == N : break
    print(time_table)
    answer = 0
    for si, li in time_table:
        answer += li-si
    return answer//N