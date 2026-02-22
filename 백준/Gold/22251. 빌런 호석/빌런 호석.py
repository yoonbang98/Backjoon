import sys
from collections import defaultdict
from itertools import product
N, K, P, X = map(int, sys.stdin.readline().split())
zero = [True, True, True, False, True, True, True]
one = [False, False, True, False, False, True, False]
two = [True, False, True, True, True, False, True]
three = [True, False, True, True, False, True, True]
four = [False, True, True, True, False, True, False]
five = [True, True, False, True, False, True, True]
six = [True, True, False, True, True, True, True]
seven = [True, False, True, False, False, True, False]
eight = [True]*7
nine = [True, True, True, True, False, True, True]
num_list = [zero, one, two, three, four ,five, six, seven, eight, nine]
dist = [[-1]*10 for _ in range(10)]
num_dict = defaultdict(list)
for idx, num in enumerate(num_list):
    num_dict[idx] = num
for i in range(10):
    for j in range(10):
        if i == j :
            dist[i][j] = 0
        else:
            if dist[i][j] != -1 : continue
            num_i = num_dict[i]
            num_j = num_dict[j]
            d = 0
            for i_tmp, j_tmp in zip(num_i, num_j):
                if i_tmp != j_tmp:
                    d += 1
            dist[i][j] = d
answer = 0
candidate = []
str_X = str(X).zfill(K)
for x in str_X:
    d_list = dist[int(x)]
    tmp = []
    for i in range(10):
        tmp.append([d_list[i], i])
    candidate.append(tmp)
for pd in product(*candidate):
    d = 0
    num_list = []
    for d_tmp, num in pd:
        d += d_tmp
        num_list.append(num)
    next_str = ''.join(map(str, num_list))
    if 1 <= int(next_str) <= N and d <= P and int(next_str) != X:
        answer += 1
print(answer)