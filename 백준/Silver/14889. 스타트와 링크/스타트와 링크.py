import sys
from itertools import combinations
N = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 대각선끼리 합
allstat = sum(sum_stat) // 2 # 모든 값 합의 절반
result = float('inf')
for l in combinations(sum_stat, N//2): # 대각선 합에서 뽑은 2개 중에서
    result = min(result, abs(allstat - sum(l))) # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀
print(result)