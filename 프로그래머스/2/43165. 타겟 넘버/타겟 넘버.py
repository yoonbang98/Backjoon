from collections import deque
def solution(numbers, target):
    answer = 0
    N = len(numbers)
    idx = 0
    queue = deque()
    queue.append([numbers[idx], idx])
    queue.append([-1*numbers[idx], idx])
    while queue:
        num, cur_idx = queue.popleft()
        if cur_idx == N-1 :
            if num == target:
                answer += 1
        else:
            next_idx = cur_idx + 1
            queue.append([num+numbers[next_idx], next_idx])
            queue.append([num-numbers[next_idx], next_idx])
        
    
    return answer