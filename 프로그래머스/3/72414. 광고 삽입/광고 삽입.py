def transform(time):
    h, m ,s = time.split(':')
    return 3600*int(h) + 60*int(m) + int(s)
def inv_transform(time):
    return str(time//3600).zfill(2) + ':' + str(time%3600//60).zfill(2) +  ':' + str(time%60).zfill(2)
def solution(play_time, adv_time, logs):
    play_time_int, adv_time_int = transform(play_time), transform(adv_time)
    time_table  = [0]*(play_time_int + 1)
    for log in logs:
        start_t, end_t = log.split('-')
        start_int, end_int = transform(start_t), transform(end_t)
        time_table[start_int] += 1
        time_table[end_int] -= 1
        
    for i in range(1, play_time_int):
        time_table[i] += time_table[i - 1]
        
    max_total = sum(time_table[:adv_time_int])  # 처음 광고가 시작될 때 누적 시청자 수
    current_total = max_total
    answer = 0

    for start_time in range(1, play_time_int - adv_time_int + 1):
        current_total = current_total - time_table[start_time - 1] + time_table[start_time + adv_time_int - 1]
        if current_total > max_total:
            max_total = current_total
            answer = start_time

    return inv_transform(answer)