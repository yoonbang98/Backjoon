def solution(routes):
    routes.sort(key = lambda x : x[1])
    key = -30001
    
    answer = 0
    
    for route in routes:
        if route[0] > key:
            answer += 1
            key = route[1]
    return answer