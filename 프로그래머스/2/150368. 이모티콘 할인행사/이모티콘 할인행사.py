from itertools import product
def solution(users, emoticons):
    answer = []
    N, M = len(users), len(emoticons)
    for p in product([10,20,30,40], repeat = M):
        result = []
        for ratio, cost_threshold in users:
            plus, cost = 0, 0
            for idx, price in enumerate(emoticons):
                if ratio <= p[idx] : cost += price*(100-p[idx])/100
            if cost >= cost_threshold :
                plus, cost = 1, 0
            result.append([plus,cost])
        total_result = [sum([i[0] for i in result]), sum([i[1] for i in result])]
        answer.append(total_result)
    answer.sort(key = lambda x : (-x[0], -x[1]))
    
    return answer[0]