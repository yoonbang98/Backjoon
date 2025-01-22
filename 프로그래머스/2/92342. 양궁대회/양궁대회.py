from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    for cwr in combinations_with_replacement([i for i in range(11)], n):
        apeach_info = [0]*11
        for s in cwr:
            apeach_info[10-s] += 1
        lion_score, apeach_score = 0, 0
        for i in range(11):
            if info[i] > apeach_info[i]: #Lion이 더 많이 맞추면
                lion_score += 10-i
            elif info[i] < apeach_info[i]: #Apeach가 더 많이 맞추면
                apeach_score += 10-i
            elif info[i] and info[i] == apeach_info[i]: #동일하게 맞추고 1개 이상 맞추면
                lion_score += 10-i
        if lion_score < apeach_score:
            answer.append([apeach_score-lion_score, apeach_info])
    if not answer :
         return [-1]
    answer.sort(key = lambda x : -x[0])
    return answer[0][1]