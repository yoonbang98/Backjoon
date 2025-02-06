import re
import copy 
from itertools import permutations
def solution(expression):
    a = re.split(r'[-*+]', expression)
    oper = set()
    oper_info  = []
    answer = 0
    for e in expression:
        if not e.isdigit():
            oper.add(e)
            oper_info.append(e)

    for per in permutations(oper, len(oper)):
        num_list = a.copy()
        oper_list = oper_info.copy()
        for operation in per:
            tmp, tmp2 = [], []
            visited = [0]*len(num_list)
            for idx, o in enumerate(oper_list):
                if o == operation:
                    
                    tmp_result = eval(str(num_list[idx]) + o + str(num_list[idx+1]))
                    num_list[idx] = tmp_result
                    num_list[idx+1] = tmp_result

                    visited[idx] = 1
                else:
                    tmp.append(o)
            oper_list = tmp
            for i, num in enumerate(num_list):
                if not visited[i]:
                    tmp2.append(num)
            num_list = tmp2

        answer = max(answer, abs(num_list[0]))
            
    return answer