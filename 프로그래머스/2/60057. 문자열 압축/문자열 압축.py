from math import inf

def solution(s):
    N = len(s)
    if N == 1:
        return 1
    answer = inf
    for length in range(1, N//2+1):
        result = ''
        pos = 0
        cnt = 1
        tmp = ''
        while True:
            if pos >= N:
                break
            if s[pos: pos + length] == tmp:
                cnt += 1
            else :
                result += tmp
                if cnt >= 2:
                    result += str(cnt)
                cnt = 1
            tmp = s[pos: pos + length]
            pos = pos + length 

        result += tmp
        if cnt >= 2:
            result += str(cnt)
        answer = min(answer, len(result))     
    return answer