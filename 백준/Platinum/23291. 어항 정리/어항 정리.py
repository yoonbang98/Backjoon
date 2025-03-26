import math
N, K = map(int, input().split())
M = int(math.ceil(math.sqrt(N)))
fish_bowl = list(map(int, input().split()))

answer = 0
dir1 = [(-1,0),(0,-1),(1,0),(0,1)] #상좌우하
dir2 = [(0,-1),(1,0),(0,1),(-1,0)] #좌하우상

def fly1(fish_bowl, M):
    field = [[0]*M for _ in range(M)]
    if M % 2 == 0:
        dir = dir2
        sr, sc = M//2 - 1, M // 2
    else:
        dir = dir1
        sr, sc = M//2, M//2
    cnt1, cnt2, d = 0, 0, 0
    thres = 1
    for fish in fish_bowl:
        field[sr][sc] = fish
        cnt1 += 1
        sr += dir[d][0]
        sc += dir[d][1]
        if cnt1 == thres:
            cnt1 = 0
            d = (d+1)%4
            cnt2 += 1
        if cnt2 == 2:
            thres += 1
            cnt2 = 0
    if M%2 == 1 :
        if not field[0][M-1]: # M이 홀수이면서 N이 제곱수가 아닌경우
            if field[M-1][M-1]: # 마지막 변의 첫 시작이 차있는 경우
                num = []
                for i in range(M-2, 0, -1):
                    if field[i][M-1]:
                        num.append(field[i][M-1])
                        field[i][M-1] = 0
                    else:
                        break
                new_M = len(field) + len(num)
                field[-1] = field[-1] + num
                for i, row in enumerate(field):
                    if len(row) != new_M:
                        field[i] = row + [0]*(new_M - len(row))
            else : #마지막 변이 아예 비었을 때
                field = list(map(list, zip(*field)))[::-1][1:]
                N, M = len(field), len(field[0])
                if field[0][M-1]:
                    return list(map(list, zip(*field[::-1])))
                num = []
                for i in range(N-2, 0, -1):
                    if field[i][M-1]:
                        num.append(field[i][M-1])
                        field[i][M-1] = 0
                    else:
                        break
                new_M = M + len(num)
                field[-1] = field[-1] + num
                for i, row in enumerate(field):
                    if len(row) != new_M:
                        field[i] = row + [0]*(new_M - len(row))

        else: # 꽉 차있는 경우 -> 시계 방향 90
            field = list(map(list, zip(*field[::-1])))
    else: #M이 짝수
        if not field[M-1][M-1]: #N이 제곱수가 아닌경우, 반시계 90
            field = list(map(list, zip(*field)))[::-1]
            if field[M-1][M-1]: # 마지막 변의 첫 시작이 차있는 경우
                num = []
                for i in range(M-2, 0, -1):
                    if field[i][M-1]:
                        num.append(field[i][M-1])
                        field[i][M-1] = 0
                    else:
                        break
                new_M = len(field) + len(num)
                field[-1] = field[-1] + num
                for i, row in enumerate(field):
                    if len(row) != new_M:
                        field[i] = row + [0]*(new_M - len(row))
            else : #마지막 변이 아예 비었을 때
                field = list(map(list, zip(*field)))[::-1][1:]
                N, M = len(field), len(field[0])
                if field[0][M-1]:
                    return list(map(list, zip(*field[::-1])))
                num = []
                for i in range(N-2, 0, -1):
                    if field[i][M-1]:
                        num.append(field[i][M-1])
                        field[i][M-1] = 0
                    else:
                        break
                new_M = M + len(num)
                field[-1] = field[-1] + num
                for i, row in enumerate(field):
                    if len(row) != new_M:
                        field[i] = row + [0]*(new_M - len(row))
        else:# 꽉 차있는 경우 -> 그대로
            pass
    return field
def fish_diff(field):
    dir = [(1,0),(0,1)]
    N, M = len(field), len(field[0])
    field_diff = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if field[r][c]:
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and field[nr][nc] and abs(field[nr][nc] - field[r][c])//5:
                        d = abs(field[nr][nc] - field[r][c])//5
                        if field[nr][nc] > field[r][c]:
                            field_diff[nr][nc] -= d
                            field_diff[r][c] += d
                        else:
                            field_diff[nr][nc] += d
                            field_diff[r][c] -= d
    for r in range(N):
        for c in range(M):
            field[r][c] += field_diff[r][c]
    return field
def fly2(fish_bowl):
    N = len(fish_bowl)
    field_tmp = []
    field_tmp.append(fish_bowl[:int(N/2)][::-1])
    field_tmp.append(fish_bowl[int(N/2):])
    field_left = []
    field_right = []
    for row in field_tmp:
        field_left.append(row[:int(N/4)])
        field_right.append(row[int(N/4):])
    for _ in range(2):
        field_left = list(map(list, zip(*field_left[::-1])))
    return field_left + field_right
max_fish, min_fish = max(fish_bowl), min(fish_bowl)
if max_fish - min_fish <= K:
    print(0)
else:
    while True:
        min_fish = min(fish_bowl)
        for idx, fish in enumerate(fish_bowl):
            if fish == min_fish:
                fish_bowl[idx] += 1

        field = fly1(fish_bowl, M)
        #print(field)
        field = fish_diff(field)
        #print(field)
        fish_bowl = []
        for c in range(len(field[0])):
            for r in range(len(field)-1, -1, -1):
                if field[r][c]:
                    fish_bowl.append(field[r][c])
                else:
                    break
        field = fly2(fish_bowl)
        field = fish_diff(field)
        #print(field)
        fish_bowl = []
        for c in range(len(field[0])):
            for r in range(len(field)-1, -1, -1):
                if field[r][c]:
                    fish_bowl.append(field[r][c])
        #print(fish_bowl)
        max_fish, min_fish = max(fish_bowl), min(fish_bowl)
        answer += 1
        if max_fish - min_fish <= K:
            break

    print(answer)