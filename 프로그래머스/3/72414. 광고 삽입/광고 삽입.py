def time_to_sec(time):
    time = list(map(int, time.split(':')))
    return time[0] * 60 * 60 + time[1] * 60 + time[2]

def sec_to_time(time):
    result, x = [], 3600
    for i in range(3):
        result.append(str(int(time//x)).zfill(2))
        time %= x
        x /= 60
    return ':'.join(result)

def solution(play_time, adv_time, logs):
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    
    # 영상의 초당 시청자 수
    time_to_total =  [0 for i in range(play_time_sec + 1)]

    # 각 구간의 시청자 수를 check 해주자
    # time_to_total[time] = time 시간에 시작된 시청자수 - time 시간에 종료된 시청자 수
    for log in logs:
        start, end = log.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        # start(초)에 시청자 1명 증가
        time_to_total[start] += 1 
        # end(초)에 시청자 1명 감소
        time_to_total[end] -= 1 

    # time_to_total[time] = time 시간부터 time + 1 시간까지 1초간의 구간을 포함한 시청자 수
    for i in range(1, len(time_to_total)):
        time_to_total[i] += time_to_total[i - 1]
    
    # time_to_total[time] = 0초 부터 time + 1 시간까지 구간을 포함한 누적 시청자 수
    for i in range(1, len(time_to_total)):
        time_to_total[i] += time_to_total[i - 1]
    
    answer = 0
    max_total = time_to_total[adv_time_sec - 1] # 0초부터 광고를 했을때 누적 시청자 수
    for current_time_sec in range(0, len(time_to_total) - adv_time_sec):
        # 현재 구간의 시청자 수의 max 갱신
        if time_to_total[current_time_sec + adv_time_sec] - time_to_total[current_time_sec] > max_total: 
            max_total = time_to_total[current_time_sec + adv_time_sec] - time_to_total[current_time_sec]
            answer = current_time_sec + 1

    return sec_to_time(answer)