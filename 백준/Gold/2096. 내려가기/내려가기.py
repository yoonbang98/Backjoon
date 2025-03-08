from math import inf
import sys
input = sys.stdin.readline
N = int(input())
field = [list(map(int, input().split()))]
if N == 1:
    print(str(max(field[0])) + ' ' + str(min(field[0])))
else:
    dir = [1,0,-1]
    for n in range(1, N):
        row = list(map(int, input().split()))
        if n == 1:
            tmp = field[0]
            tmp2 = field[0]
        dp_next = [0,0,0]
        for idx, num in enumerate(tmp):
            for d in dir:
                new_idx = idx + d
                if 0 <= new_idx < 3:
                    dp_next[new_idx] = max(dp_next[new_idx], num + row[new_idx])
        tmp = dp_next
        dp_next2 = [inf]*3
        for idx, num in enumerate(tmp2):
            for d in dir:
                new_idx = idx + d
                if 0 <= new_idx < 3:
                    dp_next2[new_idx] = min(dp_next2[new_idx], num + row[new_idx])
        tmp2 = dp_next2
    print(str(max(tmp)) + ' ' + str(min(tmp2)))