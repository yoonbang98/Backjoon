def solution(n, t, m, timetable):
    answer = 0
    time_minute = []
    for time in timetable:
        hh, mm = int(time.split(':')[0]), int(time.split(':')[1])
        time_minute.append(hh*60 + mm)
    time_minute.sort()
    now = 540 #오전 9시
    idx = 0
    for num in range(n):
        cnt = 0
        for _ in range(m):
            if idx < len(timetable) and time_minute[idx] <= now:
                idx += 1
                cnt += 1
        #print(idx, now)
        if num == n - 1: #마지막 버스 일 때
            if cnt == m : #마지막 버스 다 탔을 때
                min_value, max_value = min(time_minute[idx-m:idx]), max(time_minute[idx-m:idx])
                if min_value == max_value :
                    answer = min_value - 1
                else : 
                    answer = max_value - 1
            else: # 마지막 버스 다 안 탔을 때
                answer = now
                    
        else:
            now += t
    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)