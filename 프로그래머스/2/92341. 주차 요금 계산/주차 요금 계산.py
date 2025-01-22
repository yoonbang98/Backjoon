from collections import defaultdict
import math
def solution(fees, records):
    basic_time, basic_fee, time_unit, fee_unit = fees
    info = defaultdict(int)
    time_info = defaultdict(int)
    for record in records:
        t, car_num, in_out = record.split()
        time_num = int(t.split(':')[0])*60 + int(t.split(':')[1])
        if in_out == 'IN':
            info[car_num] = time_num
        else:
            time_info[car_num] += time_num - info[car_num]
            info[car_num] = -1
    for key, value in info.items():
        if value != -1:
            time_info[key] += 60*23 + 59 - info[key]
    answer = []
    sorted_time_info = sorted(time_info.items(), key = lambda x : x[0])
    for car_num, time in sorted_time_info:
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            fee = basic_fee + math.ceil((time-basic_time)/time_unit)*fee_unit
            answer.append(fee)
    return answer