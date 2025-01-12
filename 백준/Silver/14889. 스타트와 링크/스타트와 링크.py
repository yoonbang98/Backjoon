import sys
from itertools import combinations
N = int(sys.stdin.readline())
S_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
answer = 1e9
for com in combinations([i for i in range(N)], int(N/2)):
    #if cnt == int((N*(N-1))/4) : break
    score1, score2 = 0,0
    for p1, p2 in combinations(com, 2):
        score1 += (S_list[p1][p2]+S_list[p2][p1])
    p2_list = list(set([i for i in range(N)]) - set(com))
    for p1, p2 in combinations(p2_list, 2):
        score2 += (S_list[p1][p2]+S_list[p2][p1])
    answer = min(answer, abs(score1-score2))
    #cnt += 1
print(answer)