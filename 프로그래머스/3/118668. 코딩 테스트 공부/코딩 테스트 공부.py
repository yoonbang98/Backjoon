import heapq
from math import inf
def solution(alp, cop, problems):
    dst_alp, dst_cop = alp, cop
    for a_req, c_req, _, _, _ in problems:
        dst_alp = max(dst_alp, a_req)
        dst_cop = max(dst_cop, c_req)

    dist = [[inf]*(dst_cop+1) for _ in range(dst_alp+1)]
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    dist[alp][cop] = 0
    heap = []
    heapq.heappush(heap, [0, alp, cop])
    
    while heap:
        cur_cost, cur_r, cur_c = heapq.heappop(heap)
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req <= cur_r and cop_req <= cur_c :
                nxt_a, nxt_c = min(dst_alp, cur_r + alp_rwd), min(dst_cop, cur_c + cop_rwd)
                if dist[nxt_a][nxt_c] > cur_cost + cost:
                    heapq.heappush(heap, [cur_cost + cost, nxt_a, nxt_c])
                    dist[nxt_a][nxt_c] = cur_cost + cost

    return dist[dst_alp][dst_cop]