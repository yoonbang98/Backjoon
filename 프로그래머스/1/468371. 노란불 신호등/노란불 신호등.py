from collections import deque
def solution(signals):
    queue_list = []
    max_num = 1
    for g,y,r in signals:
        sig_list = ['G']*g + ['Y']*y + ['R']*r
        max_num *= len(sig_list)
        queue = deque(sig_list)
        queue_list.append(queue)

    answer = 1
    while True:
        if answer >= max_num:
            return -1
        new_queue_list = []
        flag = True
        for queue in queue_list:
            queue.rotate(-1)
            if queue[0] != 'Y':
                flag = False
            new_queue_list.append(queue)
        queue_list = new_queue_list
        answer += 1
        if flag:
            return answer
    return answer