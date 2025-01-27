from collections import defaultdict
def solution(id_list, report, k):
    num_report = defaultdict(int)
    report_id = defaultdict(set)
    for re in report:
        src, dst = re.split()
        if dst not in report_id[src]:
            num_report[dst] += 1
        report_id[src].add(dst)
    
    answer = []
    for id in id_list:
        report_set = report_id[id]
        tmp = 0
        for dst in report_set:
            if num_report[dst] >= k:
                tmp += 1
        answer.append(tmp)
    return answer