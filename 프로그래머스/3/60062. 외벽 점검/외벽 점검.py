from itertools import permutations
def solution(n, weak, dist):
    answer = 0
    M = len(weak)
    for i in range(M):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for s in range(M):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[s] + friends[cnt-1]
            for idx in range(s, s+M):
                if pos < weak[idx]:
                    cnt+=1
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + friends[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer