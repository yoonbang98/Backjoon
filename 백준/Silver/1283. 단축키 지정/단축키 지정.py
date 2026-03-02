import sys
from collections import defaultdict

N = int(sys.stdin.readline())
key_dict = defaultdict(list)

for _ in range(N):
    word = sys.stdin.readline().strip()
    splited_word = word.split()
    flag = False
    for idx, word in enumerate(splited_word):
        list_word = list(word)
        if list_word[0].lower() not in key_dict.keys():
            key_dict[list_word[0].lower()] = list(word)
            flag = True
            word_idx = idx
            break
    if flag:
        splited_word[word_idx] = '[' + splited_word[word_idx][0] + ']' + splited_word[word_idx][1:]
    if not flag:
        flag2 = False
        for idx, word in enumerate(splited_word):
            list_word = list(word)
            for jdx, letter in enumerate(list_word):
                if letter.lower() not in key_dict.keys():
                    key_dict[letter.lower()] = list(word)
                    flag2 = True
                    word_idx, word_idx2 = idx, jdx
                    break
            if flag2:
                break
        if flag2:
            splited_word[word_idx] = splited_word[word_idx][:word_idx2] + '[' + splited_word[word_idx][word_idx2] + ']' + splited_word[word_idx][word_idx2+1:]
    print(' '.join(splited_word))