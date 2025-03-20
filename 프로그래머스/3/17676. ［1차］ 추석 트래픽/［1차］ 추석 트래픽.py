def time_to_mili_sec(hh, mm, ss, ms):
    return int(ms) + int(ss)*1000 + int(mm)*60*1000 + int(hh)*60*60*1000
def solution(lines):
    new_line = []
    for line in lines:
        _, t, l = line.split()
        ms = t[-3:]
        t = t[:-4]
        l = l[:-1]
        hh, mm, ss = t.split(':')
        mili_sec = time_to_mili_sec(hh,mm,ss, ms)
        new_line.append([max(0,mili_sec-int(float(l)*1000) +1), mili_sec])
    answer = 0
    for s_ms, f_ms in new_line:
        src1, dst1 = s_ms, s_ms + 999
        src2, dst2 = f_ms, f_ms + 999
        result1 = 0
        result2 = 0
        for src, dst in new_line:
            if src <= dst1 and dst >= src1:
                result1 += 1
            if src <= dst2 and dst >= src2:
                result2 += 1
        answer = max(answer, result1, result2)
    return answer