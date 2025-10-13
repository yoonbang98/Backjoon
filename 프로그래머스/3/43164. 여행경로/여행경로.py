from collections import defaultdict
total_route = []
def dfs(cur, route, ticket_dict, graph, n):
    global total_route
    if len(route) == n + 1:
        total_route.append(route)
        return
    for nei in graph[cur]:  
        if ticket_dict[cur+nei]:
            ticket_dict[cur+nei] -= 1
            dfs(nei, route + [nei], ticket_dict, graph, n)
            ticket_dict[cur+nei] += 1
    return
def solution(tickets):
    n = len(tickets)
    graph = defaultdict(list)
    ticket_dict = defaultdict(int)
    for src, dst in tickets:
        graph[src].append(dst)
        ticket_dict[src+dst] += 1
        
    dfs("ICN", ['ICN'],ticket_dict, graph, n)
    total_route.sort()
    return total_route[0]