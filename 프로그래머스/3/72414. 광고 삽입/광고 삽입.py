def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

def sec_to_time(time):
    return f"{time // 3600:02}:{(time % 3600) // 60:02}:{time % 60:02}"

def solution(play_time, adv_time, logs):
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)

    # 시청자 수 변화량을 기록할 배열
    time_to_total = [0] * (play_time_sec + 2)

    # 각 구간의 시작과 끝을 반영
    for log in logs:
        start, end = map(time_to_sec, log.split('-'))
        time_to_total[start] += 1
        time_to_total[end] -= 1

    # 1차 누적합 (시청자 수 기록)
    for i in range(1, play_time_sec + 1):
        time_to_total[i] += time_to_total[i - 1]

    # 최댓값을 찾기 위한 슬라이딩 윈도우 방식 적용
    max_total = sum(time_to_total[:adv_time_sec])  # 처음 광고가 시작될 때 누적 시청자 수
    current_total = max_total
    answer = 0

    for start_time in range(1, play_time_sec - adv_time_sec + 1):
        current_total = current_total - time_to_total[start_time - 1] + time_to_total[start_time + adv_time_sec - 1]
        if current_total > max_total:
            max_total = current_total
            answer = start_time

    return sec_to_time(answer)