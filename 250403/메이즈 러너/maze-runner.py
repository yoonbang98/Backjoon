import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
field_people = [[[]for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c = map(int, input().split())
    field_people[r-1][c-1].append(1)
exit_r, exit_c = map(int, input().split())
exit_r -= 1
exit_c -= 1
field[exit_r][exit_c] = -1
dir = [(-1,0),(1,0),(0,-1),(0,1)]#상하좌우
def move(field_people, exit_r, exit_c):
    result = 0
    new_field_people = [[[]for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if field_people[r][c]:
                cur_dist = abs(r-exit_r) + abs(c-exit_c)
                nxt_cand = []
                for idx, (dr, dc) in enumerate(dir):
                    nr, nc = r + dr, c + dc
                    if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
                    nxt_dist = abs(nr-exit_r) + abs(nc-exit_c)
                    if field[nr][nc] <= 0 and cur_dist > nxt_dist:
                        nxt_cand.append([nxt_dist, idx, nr, nc])
                if not nxt_cand:
                    new_field_people[r][c] = new_field_people[r][c] + field_people[r][c]
                else:
                    result += len(field_people[r][c])
                    nxt_cand.sort()
                    nr, nc = nxt_cand[0][2], nxt_cand[0][3]
                    if (nr, nc) != (exit_r, exit_c):
                        new_field_people[nr][nc] = new_field_people[nr][nc] + field_people[r][c]
    return new_field_people, result
def square_info(field_people, exit_r, exit_c):
    min_dist = N
    for i in range(N):
        for j in range(N):
            if field_people[i][j]:
                min_dist = min(max(abs(i-exit_r), abs(j-exit_c)), min_dist)
    for i in range(N-min_dist):
        for j in range(N-min_dist):
            if i <= exit_r <= i + min_dist and j <= exit_c <= j + min_dist:
                for r in range(i, i+min_dist+1):
                    for c in range(j, j+min_dist+1):
                        if field_people[r][c]:
                            return i,j,min_dist
def turn(field, field_people, l_r, l_c, l):
    field_tmp = []
    field_people_tmp = []
    for i in range(l_r, l_r + l + 1):
        row_tmp = field[i][l_c:l_c+l+1][:]
        row  = []
        for r in row_tmp:
            if r <= 0:
                row.append(r)
            else:
                row.append(r-1)
        field_tmp.append(row)
        field_people_tmp.append(field_people[i][l_c:l_c+l+1][:])
    field_tmp = list(map(list, zip(*field_tmp[::-1])))
    field_people_tmp = list(map(list, zip(*field_people_tmp[::-1])))
    for i in range(len(field_tmp)):
        field[l_r+i][l_c:l_c+l+1] = field_tmp[i]
        field_people[l_r+i][l_c:l_c+l+1] = field_people_tmp[i]
    return field, field_people
answer = 0
for _ in range(K):
    field_people, result = move(field_people, exit_r, exit_c)
    answer += result
    cnt = 0
    for i in range(N):
        for j in range(N):
            if field_people[i][j]:
                cnt += 1
    if not cnt:
        break
    l_r, l_c, l = square_info(field_people, exit_r, exit_c)
    field, field_people = turn(field, field_people, l_r, l_c, l)
    flag = False
    for i in range(N):
        for j in range(N):
            if field[i][j] == -1:
                exit_r, exit_c = i,j
                flag = True
                break
        if flag:
            break
print(answer)
print(exit_r+1, exit_c+1)