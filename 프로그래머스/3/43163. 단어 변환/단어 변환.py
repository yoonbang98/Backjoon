from collections import deque
import copy
def solution(begin, target, words):
    answer = 1e9
    N = len(words)
    word_N = len(begin)
    visited = [False]*N
    queue = deque()
    queue.append([begin, 0, visited])
    
    while queue :
        cur_word, result, visited_tmp = queue.popleft()
        #print(visited_tmp)
        if cur_word == target:
            answer = min(answer, result)
            continue
        for idx, nxt_word in enumerate(words):
            if visited_tmp[idx] : continue
            diff_num = 0
            for i in range(word_N):
                if cur_word[i] != nxt_word[i]:
                    diff_num += 1
            if diff_num == 1:
                visited_copy = copy.deepcopy(visited_tmp)
                visited_copy[idx] = True
                queue.append([nxt_word, result + 1, visited_copy])
        
    return 0 if answer == 1e9 else answer