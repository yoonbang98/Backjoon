from itertools import permutations
from collections import defaultdict
def solution(user_id, banned_id):
    N = len(banned_id)
    possible_dict = defaultdict(int)
    for per in permutations(user_id, N):

        flag = True
        for i in range(N):
            per_i, banned_i = per[i], banned_id[i]
            if len(per_i) != len(banned_i): 
                flag = False
                break
            for j in range(len(per_i)):
                if banned_i[j] == '*' or per_i[j] == banned_i[j]: continue
                else:
                    flag = False
                    break
        if not flag: continue

        possible_dict[str(sorted(list(per)))] = 1
        
    return len(possible_dict)