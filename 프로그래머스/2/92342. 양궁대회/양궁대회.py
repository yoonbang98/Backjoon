from itertools import combinations_with_replacement
def solution(n, info):
    result = []
    for com in combinations_with_replacement([i for i in range(11)], n):
        tmp = [0]*11
        l_score, a_score = 0, 0
        for c in com:
            tmp[c] += 1
        for i in range(11):
            if info[i] >= tmp[i] and info[i]:
                a_score += 10 - i
            elif info[i] < tmp[i] and tmp[i]:
                l_score += 10 - i
        if l_score > a_score:
            tmp = "".join(str(s) for s in tmp)[::-1]
            result.append([l_score-a_score, tmp])
    if not result:
        return [-1]
    else:
        result.sort(key = lambda x : (-x[0], -int(x[1])))
        answer = []
        for r in result[0][1]:
            answer.append(int(r))
        return answer[::-1]