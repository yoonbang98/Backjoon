from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    info_dict = defaultdict(list)
    for i in info:
        splited_info = i.split()
        info_dict[splited_info[0] + splited_info[1] + splited_info[2] + splited_info[3]].append(int(splited_info[4]))
        info_dict['-' + splited_info[1] + splited_info[2] + splited_info[3]].append(int(splited_info[4]))
        info_dict[splited_info[0] + '-' + splited_info[2] + splited_info[3]].append(int(splited_info[4]))
        info_dict[splited_info[0] + splited_info[1] + '-' + splited_info[3]].append(int(splited_info[4]))
        info_dict[splited_info[0] + splited_info[1] + splited_info[2] + '-'].append(int(splited_info[4]))
        info_dict['-'+ '-' + splited_info[2] + splited_info[3]].append(int(splited_info[4]))
        info_dict['-' + splited_info[1] + '-' + splited_info[3]].append(int(splited_info[4]))
        info_dict['-' + splited_info[1] + splited_info[2] + '-'].append(int(splited_info[4]))
        info_dict[splited_info[0] + '-' + '-' + splited_info[3]].append(int(splited_info[4]))
        info_dict[splited_info[0] + '-' + splited_info[2] + '-'].append(int(splited_info[4]))
        info_dict[splited_info[0] + splited_info[1] + '-' + '-'].append(int(splited_info[4]))
        info_dict['-' + '-' + '-' + splited_info[3]].append(int(splited_info[4]))
        info_dict['-' + '-' + splited_info[2] + '-'].append(int(splited_info[4]))
        info_dict['-' + splited_info[1] + '-'  + '-'].append(int(splited_info[4]))
        info_dict[splited_info[0] + '-' + '-' + '-'].append(int(splited_info[4]))
        info_dict['-'+ '-' + '-' + '-'].append(int(splited_info[4]))
    for key, value in info_dict.items():
        info_dict[key] = sorted(value)

    answer = []
    for q in query:
        lang, job, ex, ss = q.split(' and ')
        soul, score = ss.split()
        key = lang + job + ex + soul                              
        result = len(info_dict[key]) - bisect_left(info_dict[key], int(score))
        answer.append(result)
    return answer