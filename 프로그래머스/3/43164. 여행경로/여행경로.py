from collections import defaultdict
import copy
def dfs(start, remain_tickets, edge_dict, route):
    global answer
    if answer :
        return
    if not remain_tickets: 
        answer = route
    for nei in edge_dict[start]:
        if [start, nei] in remain_tickets:
            tickets_copy = copy.deepcopy(remain_tickets)
            tickets_copy.remove([start, nei])
            dfs(nei, tickets_copy, edge_dict, route + [nei])

answer = []
def solution(tickets):
    edge_dict = defaultdict(list)
    for src, dst in tickets:
        edge_dict[src].append(dst)
    for key, value in edge_dict.items():
        value.sort()
    dfs("ICN", tickets, edge_dict, ["ICN"])
    
    return answer