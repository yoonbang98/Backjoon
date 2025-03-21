def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if b < a :
        parent[a] = b
    else:
        parent[b] = a
def solution(n, costs):
    parent = [i for i in range(n)]
    sorted_cost = sorted(costs, key = lambda x : x[2])
    
    answer = 0
    for a, b, cost in sorted_cost:
        if find_parent(parent, a) != find_parent(parent,b):
            union_parent(parent, a,b)
            answer += cost
    return answer