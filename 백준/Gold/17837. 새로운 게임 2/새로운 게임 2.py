import sys
import copy
input = sys.stdin.readline

N, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
field_horse = [[[] for _ in range(N)] for _ in range(N)]
dir = [(0,1),(0,-1),(-1,0),(1,0)] #우좌상하
for k in range(1, K+1):
    r, c, d = map(int, input().split())
    field_horse[r-1][c-1].append([k, d-1])
answer = 1

while True:
    if answer > 1000:
        answer = -1
        break
    break_param = False
    for k in range(1, K + 1):
        flag = False
        for r in range(N):
            for c in range(N):
                if not field_horse[r][c]: continue
                for idx, horse in enumerate(field_horse[r][c]):
                    if horse[0] == k:
                        horse_move = field_horse[r][c][idx:]
                        horse_not_move = field_horse[r][c][:idx]
                        field_horse[r][c] = horse_not_move

                        nr, nc = r + dir[horse[1]][0], c + dir[horse[1]][1]
                        if 0 <= nr < N and 0 <= nc < N:
                            if field[nr][nc] == 0: #흰색
                                field_horse[nr][nc] += horse_move
                            elif field[nr][nc] == 1: #빨간색
                                field_horse[nr][nc] += horse_move[::-1]
                            else: #파란색
                                if horse[1]%2 == 1:
                                    new_d = horse[1]-1
                                    nr, nc = r + dir[new_d][0], c + dir[new_d][1]
                                else:
                                    new_d = horse[1]+1
                                    nr, nc = r + dir[new_d][0], c + dir[new_d][1]
                                horse_move[0][1] = new_d
                                if 0 <= nr < N and 0 <= nc < N:
                                    if field[nr][nc] == 0: #흰색
                                        field_horse[nr][nc] += horse_move
                                    elif field[nr][nc] == 1: #빨간색
                                        field_horse[nr][nc] += horse_move[::-1]
                                    else: #파란색
                                        field_horse[r][c] += horse_move
                                else:
                                    field_horse[r][c] += horse_move
                        else :
                            if horse[1]%2 == 1:
                                new_d = horse[1]-1
                                nr, nc = r + dir[new_d][0], c + dir[new_d][1]
                            else:
                                new_d = horse[1]+1
                                nr, nc = r + dir[new_d][0], c + dir[new_d][1]
                            horse_move[0][1] = new_d
                            if field[nr][nc] == 0: #흰색
                                field_horse[nr][nc] += horse_move
                            elif field[nr][nc] == 1: #빨간색
                                field_horse[nr][nc] += horse_move[::-1]
                            else: #파란색
                                field_horse[r][c] += horse_move
                        if 0 <= nr < N and 0 <= nc < N:
                            if len(field_horse[nr][nc]) >= 4:
                                break_param = True
                        flag = True
                        break
                if flag: break
            if flag: break
        if break_param : break
    if break_param : break

    answer += 1
print(answer)
