from bisect import bisect_left, bisect_right
def count_idx(a, left_value, right_value):
    left_idx = bisect_left(a, left_value)
    right_idx = bisect_right(a, right_value)
    return right_idx - left_idx
def solution(words, queries):
    answer = []
    word = [[] for _ in range(10001)]
    word_rev = [[] for _ in range(10001)]
    
    for w in words:
        word[len(w)].append(w)
        word_rev[len(w)].append(w[::-1])
    for i in range(10001):
        word[i].sort()
        word_rev[i].sort()
        
    for query in queries:
        query_a = query.replace("?","a")
        query_z = query.replace("?","z")
        if query[0] == '?': #앞에 물음표
            s = bisect_left(word_rev[len(query)],query_a[::-1])
            e = bisect_right(word_rev[len(query)],query_z[::-1])
            answer.append(e-s)
        # ?가 접미사에 있는가?
        else:
            s = bisect_left(word[len(query)],query_a)
            e = bisect_right(word[len(query)],query_z)
            answer.append(e-s)
            
    return answer