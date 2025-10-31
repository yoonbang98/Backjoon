from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    info_dict = defaultdict(list)
    for information in info:
        score = int(information.split()[-1])
        key_list = information.split()[:-1]
        info_dict[''].append(score)
        for num in range(1, 5):
            for com in combinations(key_list, num):
                tmp = ''
                for c in com:
                    tmp += c
                info_dict[tmp].append(score)
    for key, value in info_dict.items():
        value.sort()
    answer = []
    for q in query:
        key = ''
        score = -1
        for word in q.split():
            if word == 'and' or word == '-' : continue
            if word.isdigit(): 
                score = int(word)
                continue
            key += word
        s_list = info_dict[key]

        if score != -1:
            answer.append(len(s_list) - bisect_left(s_list, score))
        else:
            answer.append(len(s_list))  
    return answer