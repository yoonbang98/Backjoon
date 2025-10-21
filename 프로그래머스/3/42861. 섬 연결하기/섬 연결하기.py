def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]
def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    answer = 0
    for i, j, cost in costs:
        if find_parent(i, parent) != find_parent(j, parent):
            union_parent(i,j, parent)
            answer += cost
    return answer