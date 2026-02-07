import sys

N, new_score, P = map(int, sys.stdin.readline().split())
if N :
    s_list = list(map(int, sys.stdin.readline().split()))
    answer = 1
    for s in s_list:
        if s > new_score:
            answer += 1
        else:
            break
    if N >= P : #랭킹 리스트에 못들수도 있음
        if answer >= P :
            if s_list[P-1] >= new_score:
                answer = -1
        if s_list[answer - 1] == s_list[P-1] and s_list[P-1] >= new_score:
            answer = -1
    print(answer)
else:
    print(1)
