import sys

N,M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
magic = []
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    magic.append([d,s])
dir = [[], [-1,0],[1,0],[0,-1],[0,1]]
answer = [0]*4

def make_1d(field):
    tmp = [0]
    r,c = N//2, N//2
    dist = 1
    cnt = 0
    cnt2 = 0
    d = 3
    while True:
        if r == 0 and c == 0:
            break
        r, c = r + dir[d][0], c + dir[d][1]
        cnt += 1
        if field[r][c] :
            tmp.append(field[r][c])
        if cnt == dist:
            cnt2 += 1
            cnt = 0
            if d == 1:
                d = 3
            elif d == 2:
                d = 4
            elif d == 3:
                d = 2
            elif d == 4:
                d = 1
        if cnt2 == 2:
            dist += 1
            cnt2 = 0
    tmp = tmp + [0]*(N**2-len(tmp))
    return tmp
def make_2d(field_1d):
    field = [[0]*N for _ in range(N)]
    r, c = N // 2, N // 2
    dist = 1
    cnt = 0
    cnt2 = 0
    d = 3

    idx = 1
    while True:
        if r == 0 and c == 0:
            break
        r, c = r + dir[d][0], c + dir[d][1]
        cnt += 1
        field[r][c] = field_1d[idx]
        if cnt == dist:
            cnt2 += 1
            cnt = 0
            if d == 1:
                d = 3
            elif d == 2:
                d = 4
            elif d == 3:
                d = 2
            elif d == 4:
                d = 1
        if cnt2 == 2:
            dist += 1
            cnt2 = 0
        idx += 1
    return field

def boom(field_1d):
    global answer
    flag = False
    tmp = field_1d[1]
    cnt = 1
    for idx, num in enumerate(field_1d):
        if idx > 1 and num and num == tmp:
            cnt += 1
        elif num and num != tmp:
            if cnt >= 4:
                flag = True
                for i in range(idx-1, idx-cnt-1, -1):
                    answer[field_1d[i]]+=1
                    field_1d[i] = 0
            cnt = 1
            tmp = num
        if not num and cnt >= 4:
            flag = True
            for i in range(idx - 1, idx - cnt - 1, -1):
                answer[field_1d[i]] += 1
                field_1d[i] = 0
            break

    return field_1d, flag

for d, s in magic:
    r,c = N//2, N//2
    for _ in range(s):
        r += dir[d][0]
        c += dir[d][1]
        field[r][c] = 0
    field_1d = make_1d(field)

    while True:
        field_1d, flag = boom(field_1d)
        if not flag: break
        new_field_1d = [0]
        for idx, num in enumerate(field_1d):
            if not idx:
                continue
            if num:
                new_field_1d.append(num)
        new_field_1d = new_field_1d + [0] * (N ** 2 - len(new_field_1d))
        field_1d = new_field_1d
    new_field_1d = [0]
    tmp = field_1d[1]
    cnt = 1
    for idx, num in enumerate(field_1d):

        if idx > 1 and num and num == tmp:
            cnt += 1
        elif num and num != tmp:
            new_field_1d.extend([cnt,tmp])
            tmp = num
            cnt = 1
    if tmp > 0 :
        new_field_1d.extend([cnt,tmp])
    if len(new_field_1d) > N*N:
        new_field_1d = new_field_1d[:N*N]
    else :
        new_field_1d = new_field_1d + [0] * (N ** 2 - len(new_field_1d))
    field_1d = new_field_1d

    field = make_2d(field_1d)


print(answer[1]+2*answer[2]+3*answer[3])