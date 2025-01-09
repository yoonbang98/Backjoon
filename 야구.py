import sys

N = int(sys.stdin.readline())
total_inning = []
for _ in range(N):
    total_inning.append(list(map(int, sys.stdin.readline().split())))
arr = [1,2,3,4,5,6,7,8]
visited = [0] * len(arr)  # visited도 전역으로 둬도 됨
result = []

def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        result.append(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0

permutations(len(arr), [])
answer = 0
for per in result:
    hitter = per[:3] + [0] + per[3:]
    inning_num = 0
    hitter_num = 0
    out = 0
    tmp = 0
    b1,b2,b3 = 0,0,0
    while True:
        if inning_num == N: #이닝 끝
            break
        hit = total_inning[inning_num][hitter[hitter_num]]
        #print(inning_num, hitter_num, hit, out)
        if hit == 0:
            out += 1
        if 1 <= hit <= 3:
            if hit == 1:
                tmp += b3
                b1, b2, b3 = 1, b1, b2
            elif hit == 2:
                tmp += b2 + b3
                b1, b2, b3 = 0, 1, b1
            else:
                tmp += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
        if hit == 4:
            tmp += b1+b2+b3+1
            b1,b2,b3 = 0,0,0
        hitter_num = (hitter_num + 1)%9
        if out > 0 and out % 3 == 0: #3아웃
            inning_num += 1
            out = 0
            b1,b2,b3 = 0,0,0
    answer = max(answer, tmp)
print(answer)