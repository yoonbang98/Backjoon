import sys
from collections import defaultdict, deque

N, K = map(int, sys.stdin.readline().split())
field = []
horse_field = [[[] for _ in range(N)] for _ in range(N)]
loc = defaultdict(int)
dir = [(0,1),(0,-1),(-1,0),(1,0)]
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,K+1):
    r,c,d = map(int, sys.stdin.readline().split())
    loc[i] = [r-1,c-1,d-1]
    horse_field[r-1][c-1].append(i)
turn = 0
break_param = False
while True:
    if break_param:
        break
    if turn == 1000:
        turn = -1
        break
    for num_horse in range(1, K + 1):
        r,c,d = loc[num_horse]
        nr = r + dir[d][0]
        nc = c + dir[d][1]

        queue = horse_field[r][c]
        if len(queue) == 1:
            horse_field[r][c] = []
        else:
            horse_idx = queue.index(num_horse)
            horse_field[r][c] = queue[:horse_idx]
            queue = queue[horse_idx:]
        #print(num_horse, horse_field)
        if 0 <= nr < N and 0 <= nc < N:
            if field[nr][nc] == 0 :#흰색
                horse_field[nr][nc].extend(queue)
                if len(horse_field[nr][nc]) >= 4:
                    break_param = True
                    break
                for num in queue:
                    loc[num][0] = nr
                    loc[num][1] = nc
            elif field[nr][nc] == 1 :#빨간색
                queue.reverse()
                horse_field[nr][nc].extend(queue)
                if len(horse_field[nr][nc]) >= 4:
                    break_param = True
                    break
                for num in queue:
                    loc[num][0] = nr
                    loc[num][1] = nc
            else : #파란색
                if d % 2 == 0:
                    d += 1
                else :
                    d -= 1
                loc[num_horse][2] = d
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if field[nr][nc] == 0:  # 흰색
                        horse_field[nr][nc].extend(queue)

                        if len(horse_field[nr][nc]) >= 4:
                            break_param = True
                            break
                        for num in queue:
                            loc[num][0] = nr
                            loc[num][1] = nc
                    elif field[nr][nc] == 1:  # 빨간색
                        queue.reverse()
                        horse_field[nr][nc].extend(queue)
                        if len(horse_field[nr][nc]) >= 4:
                            break_param = True
                            break
                        for num in queue:
                            loc[num][0] = nr
                            loc[num][1] = nc
                    else:  # 파란색
                        horse_field[r][c].extend(queue)
                else:
                    if d % 2 == 0:
                        d += 1
                    else:
                        d -= 1
                    loc[num_horse][2] = d
                    horse_field[r][c].extend(queue)
        else :
            if d % 2 == 0:
                d += 1
            else:
                d -= 1
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            loc[num_horse][2] = d
            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] == 0:  # 흰색
                    horse_field[nr][nc].extend(queue)
                    if len(horse_field[nr][nc]) >= 4:
                        break_param = True
                        break
                    for num in queue:
                        loc[num][0] = nr
                        loc[num][1] = nc
                elif field[nr][nc] == 1:  # 빨간색
                    queue.reverse()
                    horse_field[nr][nc].extend(queue)
                    if len(horse_field[nr][nc]) >= 4:
                        break_param = True
                        break
                    for num in queue:
                        loc[num][0] = nr
                        loc[num][1] = nc
                else:  # 파란색
                    horse_field[r][c].extend(queue)
            else:
                if d % 2 == 0:
                    d += 1
                else:
                    d -= 1
                loc[num_horse][2] = d
                horse_field[r][c].extend(queue)
        # print(loc)
        # print(horse_field)
    turn += 1

print(turn)