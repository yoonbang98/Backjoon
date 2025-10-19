from itertools import product

def solution(word):
    total = []
    letter = ['A', 'E', 'I', 'O', 'U']
    for num in range(1, 6):
        for com in product(letter, repeat = num):
            tmp = ''
            for l in com:
                tmp += l
            total.append(tmp)
    total.sort()
    for idx, w in enumerate(total):
        if w == word:
            return idx + 1

    answer = 0
    return answer