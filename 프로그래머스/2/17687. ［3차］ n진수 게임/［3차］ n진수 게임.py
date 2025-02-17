num_to_alpha = {'10' : 'A', '11' : 'B', '12' : 'C', '13' : 'D', '14' : 'E','15' : 'F'}
def n_number(n, num):
    start = num
    result = ''
    cnt = 0
    while start:
        tmp = str(int(start%n))
        if len(tmp) >= 2 : tmp = num_to_alpha[str(int(start%n))]
        result = tmp + result
        start = start // n
    return result

def solution(n, t, m, p):
    total_result = '0'
    for num in range(1, t*m+1):
        total_result += n_number(n, num)
    idx = 0
    answer = ''
    for _ in range(t):
        answer += total_result[idx+p-1]
        idx += m
        
    return answer