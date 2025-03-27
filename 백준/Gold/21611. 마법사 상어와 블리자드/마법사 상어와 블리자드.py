import sys
input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
magic = []
dir = [(-1,0),(1,0),(0,-1),(0,1)]#상하좌우
t_dir = [(0,-1),(1,0),(0,1),(-1,0)]#좌하우상
for _ in range(M):
    di, si = map(int, input().split())
    magic.append([di-1, si])
answer = 0
def tornado():
    t_index = []
    sr, sc = int((N-1)//2), int((N-1)//2)
    d = 0
    thres = 1
    cnt1, cnt2 = 0, 0
    while True:
        r, c = sr + t_dir[d][0], sc + t_dir[d][1]
        if c == -1:
            break
        t_index.append([r,c])
        cnt1 += 1
        if cnt1 == thres:
            cnt1 = 0
            d = (d+1)%4
            cnt2 += 1
        if cnt2 == 2:
            thres += 1
            cnt2 = 0
        sr, sc = r, c
    return t_index
t_index = tornado()
def pull(t_index, field):
    num_list = []
    for tr, tc in t_index:
        if field[tr][tc]:
            num_list.append(field[tr][tc])
    new_field = [[0]*N for _ in range(N)]
    for idx, num in enumerate(num_list):
        tr, tc = t_index[idx]
        new_field[tr][tc] = num
    return new_field
def explosion(t_index, field):
    tmp = [[0, sr, sc]]
    result = []
    for tr, tc in t_index:
        if not field[tr][tc] :
            if len(tmp) >= 4:
                result.append(tmp)
            break
        if field[tr][tc] == tmp[-1][0]: #값이 같으면
            tmp.append([field[tr][tc], tr, tc])
        else : #값이 다르면
            if len(tmp) >= 4:
                result.append(tmp)
            tmp = [[field[tr][tc], tr, tc]]
    return result
def change(t_index, field):
    new_field = [[0]*N for _ in range(N)]
    tmp = [0]
    result = []
    for tr, tc in t_index:
        if not field[tr][tc]:
            if tmp[-1]:
                result.append(len(tmp)) #A
                result.append(tmp[-1])#B
            break
        if field[tr][tc] == tmp[-1]: #값이 같으면
            tmp.append(field[tr][tc])
        else : #값이 다르면
            if tmp[-1]:
                result.append(len(tmp)) #A
                result.append(tmp[-1])#B
            tmp = [field[tr][tc]]
    for idx, num in enumerate(result):
        if idx == N**2 - 1:
            break
        tr, tc = t_index[idx]
        new_field[tr][tc] = num
    return new_field
for di, si in magic:
    sr, sc = int((N-1)//2), int((N-1)//2)
    r, c = sr, sc
    for _ in range(si):
        r += dir[di][0]
        c += dir[di][1]
        field[r][c] = 0
    field = pull(t_index, field)
    while True:
        result = explosion(t_index, field)
        if not result :
            break
        for group in result:
            for val, r, c in group:
                answer += val
                field[r][c] = 0
        field = pull(t_index, field)
    field = change(t_index, field)
print(answer)