import sys
from collections import defaultdict
N = int(sys.stdin.readline())
word_list = []
max_length = 0
for n in range(N):
    word = str(sys.stdin.readline().strip())
    max_length = max(max_length, len(word))
    word_list.append([n,word])
answer_prefix = ''
for L in range(1, max_length+1):
    word_dict = defaultdict(list)
    for n, word in word_list:
        if len(word) >= L:
            if word_dict[word[:L]]:
                word_dict[word[:L]] = [word_dict[word[:L]][0] + 1, word_dict[word[:L]][1]]
            else:
                word_dict[word[:L]] = [1, n]
    sorted_word_dict = sorted(word_dict.items(), key = lambda x : x[1][1])
    for k, v in sorted_word_dict:
        if v[0] >= 2:
            answer_prefix = k
            break
            
L = len(answer_prefix)
S, T = '', ''
for _, word in word_list:
    if word[:L] == answer_prefix and not S:
        S = word
        continue
    if word[:L] == answer_prefix and S and not T:
        T = word
        break
print(S)
print(T)
