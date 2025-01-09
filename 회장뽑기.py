import sys

N = int(sys.stdin.readline())
graph = [[1e9]*(N+1) for _ in range(N+1)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
for n in range(1, N+1):
    graph[n][n] = 0
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
longest = []
for n in range(1, N+1):
    nei_list = graph[n][1:]
    longest.append([max(nei_list), n])
longest.sort()
answer_num = longest[0][0]
tmp = 0
hubo = []
for l_list in longest:
    if l_list[0] == answer_num:
        tmp += 1
        hubo.append(l_list[1])
    else:
        break
print(str(answer_num) + ' ' + str(tmp))
print(*hubo)