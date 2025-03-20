import bisect
def solution(words, queries):
    new_words = []
    new_r_words = []
    for word in words:
        new_words.append([len(word), word])
        new_r_words.append([len(word), word[::-1]])
    new_words.sort()
    new_r_words.sort()
    answer = []
    for q in queries:
        if q[0] != '?':
            q_a = q.replace('?', 'a')
            q_z = q.replace('?', 'z')
            left_idx = bisect.bisect_left(new_words, [len(q),q_a])
            right_idx = bisect.bisect_right(new_words, [len(q),q_z])
            answer.append(right_idx - left_idx)
        else:
            q_a = q.replace('?', 'a')[::-1]
            q_z = q.replace('?', 'z')[::-1]
            left_idx = bisect.bisect_left(new_r_words, [len(q),q_a])
            right_idx = bisect.bisect_right(new_r_words, [len(q),q_z])
            answer.append(right_idx - left_idx)
    return answer