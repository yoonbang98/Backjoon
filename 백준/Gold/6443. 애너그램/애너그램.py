from collections import defaultdict
N = int(input())
def dfs(result):
    if len(result) == M:
        print(result)
        return
    for k, v in word_dict.items():
        if v :
            word_dict[k] -= 1
            dfs(result + k)
            word_dict[k] += 1
    return
for _ in range(N):
    word = str(input())
    word = sorted(word)
    M = len(word)
    word_dict = defaultdict(int)
    for letter in word:
        word_dict[letter] += 1
    dfs('')
