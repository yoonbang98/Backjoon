from collections import defaultdict
def solution(message, spoiler_ranges):
    m_split = message.split()
    spo = [False]*len(m_split)
    if message[0] == ' ': 
        loc = 1
    else:
        loc = 0
    for idx, word in enumerate(m_split):
        l_idx, r_idx = loc, loc + len(word) - 1
        
        for src, dst in spoiler_ranges:
            for j in range(src, dst + 1):
                if l_idx <= j <= r_idx:
                    spo[idx] = True
                    break
        loc += len(word) + 1
    word_dict = defaultdict(int)
    for idx, word in enumerate(m_split):
        if not spo[idx]:
            word_dict[word] += 1
    
    answer = 0
    spo_word = []
    for idx, word in enumerate(m_split):
        if spo[idx] :
            if not word_dict[word] and word not in spo_word:
                answer += 1
            spo_word.append(word)
    return answer