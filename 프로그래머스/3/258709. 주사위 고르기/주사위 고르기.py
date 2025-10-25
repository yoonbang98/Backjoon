from itertools import combinations, product
def solution(dice):
    N = len(dice)
    answer = []
    visited = []
    max_num = 0
    for a_com in combinations([i for i in range(N)], int(N/2)):
        b_com = list(set([i for i in range(N)]) - set(a_com))
        if a_com in visited : continue
        visited.append(list(a_com))
        visited.append(b_com)
        a_dice = [dice[a] for a in a_com]
        b_dice = [dice[b] for b in b_com]
        result = [0]*501
        for pro in product(*a_dice):
            result[sum(pro)] += 1
        win_number, lose_number = 0, 0
        for pro2 in product(*b_dice):
            win_number += sum(result[sum(pro2) + 1:])
            lose_number += sum(result[:sum(pro2)])
        answer.append([win_number, a_com])
        answer.append([lose_number, b_com])
    answer.sort(key = lambda x : -x[0])
    answer_final = []
    for a in answer[0][1]:
        answer_final.append(a+1)
    return answer_final
