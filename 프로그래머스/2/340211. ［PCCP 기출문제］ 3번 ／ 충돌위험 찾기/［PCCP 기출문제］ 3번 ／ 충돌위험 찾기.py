from collections import defaultdict, Counter

def solution(points, routes):
    answer = 0
    dic = defaultdict(list)
    
    for route in routes:    
        path = []
        idx = 0
        for i in range(1, len(route)):
            x, y = points[route[i-1]-1][0], points[route[i-1]-1][1]
            target_x, target_y = points[route[i]-1][0], points[route[i]-1][1]
            
            if i == 1:
                dic[idx].append((x,y))
            
            while x != target_x:
                if x < target_x:
                    x+=1
                else:
                    x-=1
                idx+=1
                dic[idx].append((x,y))
            
            while y != target_y:
                if y < target_y:
                    y+=1
                else:
                    y-=1
                idx+=1
                dic[idx].append((x,y))
    for key in dic:
        c = Counter(dic[key])
        for key in c:
            if c[key] > 1:
                answer += 1
    
    return answer