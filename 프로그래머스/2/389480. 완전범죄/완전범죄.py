
answer = 121
check = set()
def dfs(info, n, m, a_tmp, b_tmp, i):
    global answer
    # print(a_tmp, b_tmp, visited)
    
    if a_tmp >= n or b_tmp >= m : return
    
    if (i, a_tmp, b_tmp) in check: return
    check.add((i, a_tmp, b_tmp))
    
    if i == len(info):
        answer = min(answer, a_tmp)
        return
    
    a, b = info[i][0], info[i][1]
    dfs(info, n, m, a_tmp, b_tmp + b, i + 1)
    dfs(info, n, m, a_tmp + a, b_tmp, i + 1)

    return
    
def solution(info, n, m):
    N = len(info)
    dfs(info, n, m, 0, 0, 0)
    if answer == 121:
        return -1
    return answer