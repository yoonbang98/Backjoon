import math
def solution(lines):
    answer = 0
    if len(lines) == 1:
        answer = 1
        return answer
    log = []
    for line in lines:
        date,s,t = line.split()
        s = s.split(':')
        t = t.replace('s', '')
        end = (int(s[0])*3600 + int(s[1])*60 + float(s[2]))*1000
        start = end - float(t)*1000 + 1
        
        log.append([start, end])
    #print(log)
    for x in log:
        answer = max(answer, throughput(log, x[0], x[0] + 1000), throughput(log, x[1], x[1] + 1000))
    return answer
def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt