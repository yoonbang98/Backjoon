import sys
sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    v = int(sys.stdin.readline())
    graph[v].append(i)

def dfs(u, visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            for i in visited:
                answer.add(i)
answer = set()
for i in range(1, N+1):
    dfs(i, set([]))
answer = list(answer)
answer.sort()
print(len(answer))
for a in answer:
    print(a)
