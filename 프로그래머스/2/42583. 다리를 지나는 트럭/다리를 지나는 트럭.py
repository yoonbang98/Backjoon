from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    answer = 0
    bridge = [0]*bridge_length
    while queue:
        new_truck = queue.popleft()
        if sum(bridge) + new_truck > weight: #무게 넘어갈 경우
            cnt = 0
            while True:
                bridge.pop()
                cnt += 1
                if sum(bridge) + new_truck <= weight:
                    bridge = [new_truck] + [0]*(cnt-1) + bridge
                    break
            answer += cnt
        else: #무게 안넘어갈 경우
            bridge.pop()
            bridge = [new_truck] + bridge
            answer += 1
    for idx, t in enumerate(bridge):
        if t:
            answer += bridge_length - idx
            break
    
    return answer