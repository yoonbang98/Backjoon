import math

def solution(n, bans):
    table = {}
    for idx, value in enumerate(list('abcdefghijklmnopqrstuvwxyz'), 1):
        table[value] = idx
    
    bans = sorted(bans, key=lambda x: (len(x), x))

    actual_number = n
    # 앞에서 삭제된 거 찾기   
    for string in bans:
        string_list = list(reversed(string))
        number = 0
        for idx in range(len(string)):
            number += (math.pow(26, idx) * table[string_list[idx]])
        if number > actual_number:
            break
        actual_number += 1

    # n을 26진수로 표현
    n_26 = []
    while actual_number > 0:
        share = actual_number // 26
        remainer = actual_number % 26
        if remainer == 0:
            remainer = 26
            share -= 1
        n_26.append(remainer)
        actual_number = share
    
    n_26.reverse()

    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    answer = []
    for value in n_26:
        answer.append(alphabets[value-1])
    
    return "".join(answer)