import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

data = [[False]*(n+1) for _ in range(h+1)]


#데이터 입력받기
for _ in range(m):
    x,y = map(int,input().split())
    data[x][y] = True
    
    

#현재 그래프 상태에서 조건을 만족하는지 판단.    
def check(data):
    for i in range(1,n):
        my_num = i
        for j in range(1,h+1):
            #내려가던중 오른쪽으로 선있으면 숫자 +1
            if data[j][my_num]:
                my_num += 1
            #내려가던중 왼쪽에 선있으면 숫자 -1
            elif data[j][my_num-1]:
                my_num -= 1
            
        if my_num != i:
            return False
        
    return True

result = 4
#전체 탐색을 위한 재귀 함수
def dfs(depth, data, x,y):
    global result
    if depth >= result:
        return
    
    #주어진 사다리가 조건을 충족하면 결과 갱신
    if check(data):
        result = min(result, depth)
        return
    
    if depth == 3:
        return
  
    #현재 깊이에서 안되면 다음 깊이 탐색                
    for i in range(x,h+1):
        ########################
        if x == i:
            k = y
        else:
            k = 0
        ########################
        for j in range(k,n):
            if data[i][j] == False and data[i][j+1] == False and data[i][j-1] == False:
                data[i][j] = True
                #방금 추가해준 사다리 위치를 기억하고 그다음 사다리부터 추가되도록 작성
                #추가된 좌표를 하나의 값으로 바꿔서 다다음 함수로 보냄
                dfs(depth+1,data, i ,j+2)
                data[i][j] = False
                    
    
dfs(0,data,1,1)
if result == 4:
    result = -1
    
print(result)