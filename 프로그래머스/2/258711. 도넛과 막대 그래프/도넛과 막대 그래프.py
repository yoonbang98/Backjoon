def solution(edges):
    N = 0
    answer = [0,0,0,0]
    for src, dst in edges:
        N = max(N, src, dst)
    exist = [False]*(N+1)
    edge_list = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    for src, dst in edges:
        edge_list[src].append(dst)
        exist[src] = True
        exist[dst] = True
        indegree[dst] += 1
    gen = 0
    gen_out = 0
    for n in range(1,N+1):
        if exist[n] and not indegree[n] and gen_out < len(edge_list[n]):
            gen_out = len(edge_list[n])
            gen = n
    answer[0] = gen
    for start in edge_list[gen]:
        indegree[start] -= 1
    for start in range(1,N+1):
        if not exist[start] : continue
        if indegree[start] == 2:
            answer[3] += 1
        if not indegree[start] and start != gen:
            answer[2] += 1
    answer[1] = len(edge_list[gen]) - answer[2] - answer[3]
    return answer
