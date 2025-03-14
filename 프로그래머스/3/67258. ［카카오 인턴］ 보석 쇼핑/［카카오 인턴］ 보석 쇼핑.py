from collections import defaultdict
def solution(gems):
    N = len(set(gems))
    M = len(gems)
    
    gem_dict = defaultdict(int)
    answer_L = 1e6
    start, end = 0, 0
    answer = [1,1]
    gem_dict[gems[0]] = 1
    while start <= end and end < M:  
        if len(gem_dict.keys()) == N:
            if answer_L > end - start:
                answer_L = end - start
                answer = [start + 1, end + 1]
            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1
            start += 1
            
        else :
            end += 1
            if end < M:
                gem_dict[gems[end]] += 1
            
        
    
    return answer