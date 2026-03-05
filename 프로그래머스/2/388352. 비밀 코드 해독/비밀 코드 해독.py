from itertools import combinations

def solution(n, q, ans):
    answer = 0
    M = len(q)
    for com in combinations([i for i in range(1, n+1)], 5):
        flag = True
        for i in range(M):
            q_tmp = q[i]
            a_tmp = ans[i]
            if len(set(com) & set(q_tmp)) != a_tmp:
                flag = False
                break
        if flag:
            answer += 1
    
    return answer