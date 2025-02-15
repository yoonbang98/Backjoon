from itertools import combinations
def solution(relation):
    total_result = []
    N = len(relation[0])
    for n in range(1, N+1):
        for comb in combinations([i for i in range(N)], n):
            tmp = set()
            for rel in relation :
                word = ''
                for c in comb :
                    word += rel[c]
                tmp.add(word)
            if len(tmp) == len(relation):
                if not total_result: 
                    total_result.append(comb)
                    continue
                flag = True
                for unique in total_result:
                    #print(set(unique), set(comb), set(unique) & set(comb))
                    if len(set(unique) & set(comb)) == min(len(set(unique)), len(set(comb))):
                        flag = False
                        break
                if flag:
                    total_result.append(comb)
    return len(total_result)