def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0 #배달 카운트
    pickup = 0 #수거 카운트
    
    for i in range(n-1, -1, -1): #뒤에서 부터 배달, 수거 함
        delivery += deliveries[i] #배달 카운트에 현재 집의 배달 갯수 더함
        pickup += pickups[i] #수거 카운트에 현재 집의 수거 갯수 더함
        
        while delivery > 0 or pickup > 0: #배달카운트와 수거카운트 중 하나라도 0보다 크면 (현재 집에 배달, 수거해야 할 택배가 남아 있어 추가 방문 필요)
            delivery -= cap #배달 카운트 - 트럭 용적량
            pickup -= cap #수거 카운트 - 트럭 용적량
            answer += (i+1) * 2 #거리 계산
    
    return answer