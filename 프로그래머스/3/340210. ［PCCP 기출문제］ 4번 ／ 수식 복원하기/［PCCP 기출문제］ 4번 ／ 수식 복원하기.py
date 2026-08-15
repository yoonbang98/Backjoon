def n_to_10(n, num):
    if len(num) == 3:
        return int(num[0]) * n**2 + int(num[1]) * n + int(num[2])
    elif len(num) == 2:
        return int(num[0])* n + int(num[1])
    else:
        return int(num)
def ten_to_n(n, num):
    if num//(n**2):
        return str(num//(n**2)) + str(num%(n**2)//n) + str(num%n)
    elif num//(n):
        return str(num//n) + str(num%n)
    else:
        return str(num)
def solution(expressions):
    num_set = set()
    for exp in expressions:
        num_1, oper, num_2, _, num_3 = exp.split()
        for letter in num_1 :
            if letter != 'X':
                num_set.add(letter)
        for letter in num_2:
            if letter != 'X':
                num_set.add(letter)
        for letter in num_3:
            if letter != 'X':
                num_set.add(letter)
    possible_n = [n for n in range(2, 10) if n > int(max(num_set))]
    if len(possible_n) >= 2:
        for exp in expressions:
            if 'X' not in exp:
                num_1, oper, num_2, _, num_3 = exp.split()
                possible_n_copy = possible_n[:]
                for n in possible_n : 
                    num_1_10, num_2_10, num_3_10 = n_to_10(n, num_1), n_to_10(n, num_2), n_to_10(n, num_3)
                    if oper == '+':
                        if num_1_10 + num_2_10 != num_3_10:
                            possible_n_copy.remove(n)
                    if oper == '-':
                        if num_1_10 - num_2_10 != num_3_10:
                            possible_n_copy.remove(n)
                possible_n = possible_n_copy
    answer = []
    for exp in expressions:
        if 'X' in exp:
            possible_x = set()
            for n in possible_n:
                num_1, oper, num_2, _, _ = exp.split()
                num_1_10, num_2_10 = n_to_10(n, num_1), n_to_10(n, num_2)
                if oper == '+' :
                    result_10 = num_1_10 + num_2_10
                if oper == '-':
                    result_10 = num_1_10 - num_2_10
                result_n = ten_to_n(n, result_10)
                possible_x.add(result_n)
            if len(possible_x) >= 2:
                answer.append(exp.replace('X', '?'))
            else:
                answer.append(exp.replace('X', list(possible_x)[0]))
    
    return answer