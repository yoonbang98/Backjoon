import sys
from collections import defaultdict
from itertools import chain
def rc_calculate(arr, mode):
    max_length = 0
    sorted_row = []
    for row in arr:
        tmp_dict = defaultdict(int)
        for num in row:
            if num != 0:
                tmp_dict[num] += 1
        s_row = list(chain(*sorted(tmp_dict.items(), key=lambda x: (x[1], x[0]))))
        max_length = max(max_length, len(s_row))
        sorted_row.append(s_row)
    for s_row in sorted_row:
        s_row += [0]*(max_length-len(s_row))
        if len(s_row) > 100:
            s_row = s_row[:100]
    return sorted_row if mode =='R' else list(map(list, zip(*sorted_row)))

R,C,K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, sys.stdin.readline().split())))

correct = False
for t in range(0,101):
    c_len = len(arr[0])
    r_len = len(arr)
    if R <= r_len and C <= c_len and arr[R-1][C-1] == K:
        print(t)
        correct = True
        break
    else:
        if r_len >= c_len:
            arr = rc_calculate(arr,'R')
        else :
            arr = rc_calculate(list(map(list, zip(*arr))), 'C')
if t == 100 and not correct:
    print(-1)


