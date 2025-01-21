from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    if (q1_sum + q2_sum)%2 == 1 :
        return -1
    half = (q1_sum + q2_sum)/2
    N = len(q1)
    for i in range(N):
        if q1[i] > half or q2[i] > half :
            return -1
    answer = 0
    while True:
        if answer >= 4*N:
            return -1
        if q1_sum == half :
            return answer
        if q1_sum > half:
            q1_pop = q1.popleft()
            q2.append(q1_pop)
            q1_sum -= q1_pop
            q2_sum += q1_pop
        else:
            q2_pop = q2.popleft()
            q1.append(q2_pop)
            q2_sum -= q2_pop
            q1_sum += q2_pop
        answer += 1   
    