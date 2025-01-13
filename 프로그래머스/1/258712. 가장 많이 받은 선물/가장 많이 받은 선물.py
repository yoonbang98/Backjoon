from collections import defaultdict
from itertools import combinations
def solution(friends, gifts):
    N = len(friends)
    answer = [0]*N
    idx_dict = defaultdict(int)
    for idx, name in enumerate(friends):
        idx_dict[name] = idx
    adj = [[0]*N for _ in range(N)]
    for gift in gifts:
        src, dst = gift.split()
        adj[idx_dict[src]][idx_dict[dst]] += 1
    for com in combinations(friends, 2):
        src_idx, dst_idx = idx_dict[com[0]], idx_dict[com[1]]
        if adj[src_idx][dst_idx] or adj[dst_idx][src_idx]: #주고 받은 기록 있다면
            if adj[src_idx][dst_idx] == adj[dst_idx][src_idx]: #주고 받은 수가 같다면 
                src_gift = sum(adj[src_idx]) - sum([i[src_idx] for i in adj])
                dst_gift = sum(adj[dst_idx]) - sum([i[dst_idx] for i in adj])
                if src_gift == dst_gift: 
                    continue
                elif src_gift > dst_gift:
                    answer[src_idx] += 1
                else :
                    answer[dst_idx] += 1
            elif adj[src_idx][dst_idx] > adj[dst_idx][src_idx]:
                answer[src_idx] += 1
            else:
                answer[dst_idx] += 1
        else : #주고받은 기록 x
            src_gift = sum(adj[src_idx]) - sum([i[src_idx] for i in adj])
            dst_gift = sum(adj[dst_idx]) - sum([i[dst_idx] for i in adj])
            if src_gift == dst_gift: 
                continue
            elif src_gift > dst_gift:
                answer[src_idx] += 1
            else :
                answer[dst_idx] += 1
    
    return max(answer)