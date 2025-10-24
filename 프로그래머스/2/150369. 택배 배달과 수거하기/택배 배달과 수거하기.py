def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0
    pickup = 0
    
    for i in range(n-1, -1 ,-1):
        deliver += deliveries[i]
        pickup += pickups[i] 
        
        while deliver > 0 or pickup > 0: 
            deliver -= cap 
            pickup -= cap 
            answer += (i+1) * 2
    return answer