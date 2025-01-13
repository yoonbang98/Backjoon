from itertools import combinations, product
from collections import defaultdict
def solution(dice):
    N = len(dice)
    answer = []
    visited = []
    for com in combinations([i for i in range(N)], int(N/2)):
        if list(com) in visited: continue
        visited.append(list(com))
        counter_dice = list(set([i for i in range(N)])-set(com))
        dice_list = []
        for n in com:
            dice_list.append(dice[n])
        counter_dice_list = []
        for n in counter_dice:
            counter_dice_list.append(dice[n])
        visited.append(counter_dice)    
        result = [0]*501
        for per in product(*dice_list):
            result[sum(per)] += 1
        win_number, lose_number = 0, 0
        for per in product(*counter_dice_list):
            win_number += sum(result[sum(per)+1:])
            lose_number += sum(result[:sum(per)])
        answer.append(list(com) + [win_number])
        answer.append(counter_dice + [lose_number])

    answer.sort(key = lambda x : -x[-1])
    answer = answer[0][:-1]
    for idx, a in enumerate(answer):
        answer[idx] += 1
    return answer