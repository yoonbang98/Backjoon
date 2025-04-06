import sys

input = sys.stdin.readline
N = int(input())
command = []
for _ in range(N):
    t, r, c = map(int, input().split())
    command.append([t,r,c])

green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]

score = 0
def make_score(field, mode):
    score = 0
    if mode == 'b':
        field = list(map(list, zip(*field[::-1])))
    new_field = []
    for i in range(6):
        if i <= 1:
            new_field.append(field[i])
        else:
            if field[i] == [1,1,1,1]:
                score += 1
            else:
                new_field.append(field[i])
    if score:
        add = [[0]*4 for _ in range(score)]
        new_field = add + new_field
    cnt = 0
    for i in range(2):
        if 1 in new_field[i]:
            cnt += 1
    for _ in range(cnt):
        new_field.pop()
    if cnt:
        add = [[0]*4 for _ in range(cnt)]
        new_field = add + new_field
    if mode == 'b':
        return list(map(list, zip(*new_field)))[::-1], score
    else:
        return new_field, score
for t, r, c in command:
    if t == 1:
        g_sr, g_sc = 0, c
        while True:
            if not green[g_sr+1][g_sc]:
                g_sr += 1
                if g_sr == 5:
                    break
            else :
                break
        green[g_sr][g_sc] = 1
        b_sr, b_sc = r, 0
        while True:
            if not blue[b_sr][b_sc+1]:
                b_sc += 1
                if b_sc == 5:
                    break
            else :
                break
        blue[b_sr][b_sc] = 1
    elif t == 2:
        g_sr, g_sc = 0, c
        while True:
            if not green[g_sr+1][g_sc] and not green[g_sr+1][g_sc+1]:
                g_sr += 1
                if g_sr == 5:
                    break
            else :
                break
        green[g_sr][g_sc], green[g_sr][g_sc+1] = 1, 1
        b_sr, b_sc = r, 0
        while True:
            if not blue[b_sr][b_sc+1]:
                b_sc += 1
                if b_sc == 5:
                    break
            else :
                break
        blue[b_sr][b_sc] , blue[b_sr][b_sc-1] = 1, 1
    else:
        g_sr, g_sc = 0, c
        while True:
            if not green[g_sr+1][g_sc]:
                g_sr += 1
                if g_sr == 5:
                    break
            else :
                break
        green[g_sr][g_sc], green[g_sr-1][g_sc] = 1, 1
        b_sr, b_sc = r, 0
        while True:
            if not blue[b_sr][b_sc+1] and not blue[b_sr+1][b_sc+1]:
                b_sc += 1
                if b_sc == 5:
                    break
            else :
                break
        blue[b_sr][b_sc] , blue[b_sr+1][b_sc] = 1, 1
    green, score_g = make_score(green, 'g')
    blue, score_b = make_score(blue, 'b')
    score += (score_g + score_b)
result = 0
for i in range(6):
    for j in range(4):
        if green[i][j] :
            result += 1
for i in range(4):
    for j in range(6):
        if blue[i][j] :
            result += 1
print(score)
print(result)