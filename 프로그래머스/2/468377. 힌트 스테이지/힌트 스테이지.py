from collections import defaultdict
answer = 1e9

def dfs(cost, hint, result, depth, hint_dict):
    global answer
    if depth == len(cost) - 1:
        hint_num = hint_dict[len(cost)]
        
        answer = min(answer, result + cost[depth][min(hint_num, len(cost) - 1)])
        return
    cur_cost, cur_hint = cost[depth], hint[depth]
    hint_dict_copy = hint_dict.copy()
    for idx, n in enumerate(cur_hint):
        if not idx : continue
        hint_dict_copy[n] += 1
    
    if depth == 0: #힌트 사용 못함
        cur_result = result + cur_cost[0]
        
        dfs(cost, hint, cur_result + cur_hint[0], depth + 1, hint_dict_copy) # 힌트 삼
        dfs(cost, hint, cur_result, depth + 1, hint_dict) # 힌트 안삼
    else: #힌트 사용 가능
        possible_hint = 0
        for k, v in hint_dict.items():
            if k == depth + 1:
                possible_hint = v
        if possible_hint >= len(cost) - 1:
            possible_hint = len(cost) - 1
        cur_result = result + cur_cost[possible_hint]
        dfs(cost, hint, cur_result, depth + 1, hint_dict)
        
        possible_hint2 = 0
        for k, v in hint_dict_copy.items():
            if k == depth + 1:
                possible_hint2 = v
        if possible_hint2 >= len(cost) - 1:
            possible_hint2 = len(cost) - 1
        cur_result = result + cur_cost[possible_hint2]
        dfs(cost, hint, cur_result + cur_hint[0], depth + 1, hint_dict_copy) #힌트 삼
    
    
def solution(cost, hint):
    hint_dict = defaultdict(int)
    dfs(cost, hint, 0, 0, hint_dict)
    return answer