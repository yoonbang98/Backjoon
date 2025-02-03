from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    menu_dict = defaultdict(int)
    for order in orders:
        for num in course:
            for com in combinations(order, num):
                menu_dict["".join(sorted(list(com)))] += 1
    for num in course:
        max_num = 0
        for key, value in menu_dict.items():
            if len(key) == num:
                max_num = max(max_num, value)
        for key, value in menu_dict.items():
            if len(key) == num and value == max_num and value >= 2:
                answer.append(key)

    return sorted(answer)