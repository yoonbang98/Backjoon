
def solution(schedules, timelogs, startday):
    answer = 0
    
    N = len(schedules)
    for n in range(N):
        sche = schedules[n]
        log = timelogs[n]
        startday_copy = startday
        flag = True
        for i in range(7):
            log_tmp = log[i]
            if startday_copy >= 6: 
                startday_copy += 1
                if startday_copy == 8:
                    startday_copy = 1
                continue
            if sche//100*60 + sche%100 + 10 < log_tmp//100*60 + log_tmp%100:
                flag = False
                break
            else:
                startday_copy += 1
        if flag:
            answer += 1
    return answer