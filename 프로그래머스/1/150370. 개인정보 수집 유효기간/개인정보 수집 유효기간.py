from collections import defaultdict
def solution(today, terms, privacies):
    t_yy, t_mm, t_dd = today.split('.')
    threshold = int(t_yy)*10000 + int(t_mm)*100 + int(t_dd)

    term_dict = defaultdict(int)
    answer = []
    for term in terms:
        t_type, period = term.split()
        term_dict[t_type] = int(period)
    for idx, privacy in enumerate(privacies):
        yy, mm, dd = privacy.split()[0].split('.')
        t_type = privacy.split()[1]
        period = term_dict[t_type]
        if int(dd) == 1:
            mm, dd =(int(mm) + period%12-1),28
            if mm > 12:
                mm -= 12
                yy = int(yy) + period//12 + 1
            else :
                yy = int(yy) + period//12
        else :
            mm, dd = (int(mm) + period%12), int(dd) -1
            if mm > 12:
                mm -= 12
                yy = int(yy) + period//12 + 1
            else :
                yy = int(yy) + period//12
        if threshold > int(yy)*10000 + int(mm)*100 + int(dd):
            answer.append(idx + 1)
    return answer