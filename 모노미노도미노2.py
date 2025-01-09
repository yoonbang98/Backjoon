import sys
from collections import deque
green = deque()
blue = deque()
for _ in range(6):
    green.append([0] * 4)
    blue.append([0] * 4)

N = int(sys.stdin.readline())
score = 0
for _ in range(N):
    t,x,y = map(int, sys.stdin.readline().split())
    if t == 1:
        r = 0
        while r <= 5:
            if green[r][y]:
                break
            r += 1
        green[r-1][y] = 1

        r = 0
        while r <= 5:
            if blue[r][abs(3-x)]:
                break
            r += 1
        blue[r - 1][abs(3-x)] = 1
    elif t == 2:
        r = 0
        while r <= 5:
            if green[r][y] or green[r][y+1]:
                break
            r += 1
        green[r - 1][y] = 1
        green[r - 1][y + 1] = 1

        r = 0
        while r <= 5:
            if blue[r][abs(3-x)]:
                break
            r += 1
        blue[r - 1][abs(3-x)] = 1
        blue[r - 2][abs(3-x)] = 1
    elif t == 3:
        r = 0
        while r <= 5:
            if green[r][y]:
                break
            r += 1
        green[r - 1][y] = 1
        green[r - 2][y] = 1

        r = 0
        while r <= 5:
            if blue[r][abs(3-x)] or blue[r][abs(3-x) -1]:
                break
            r += 1
        blue[r - 1][abs(3-x)] = 1
        blue[r - 1][abs(3-x) -1] = 1
    for idx in range(6):
        row = green[idx]
        row2 = blue[idx]
        if sum(row) == 4:
            score += 1
            del green[idx]
            green.appendleft([0]*4)
        if sum(row2) == 4:
            score += 1
            del blue[idx]
            blue.appendleft([0]*4)
    green_cnt = 0
    blue_cnt = 0
    for i in range(2):
        if sum(green[i]) > 0:
            green_cnt += 1
        if sum(blue[i]) > 0:
            blue_cnt += 1
    for _ in range(green_cnt):
        green.pop()
        green.appendleft([0]*4)
    for _ in range(blue_cnt):
        blue.pop()
        blue.appendleft([0]*4)
tile = 0
for i in range(6):
    tile += sum(green[i])
    tile += sum(blue[i])

print(score)
print(tile)

