import sys
from collections import deque

N = int(sys.stdin.readline())

def bfs():
    while queue:
        r,c,case = queue.popleft()
        if case == 'S' and (r == 0 or r == h-1 or c == 0 or c == w-1):
            if field[r][c] == '#':
                continue
            return field[r][c] + 1
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if field[nr][nc] != '#' and case == 'F':
                    field[nr][nc] = '#'
                    queue.append((nr,nc, 'F'))
                elif field[nr][nc] == '.' and case == 'S' and field[r][c] != '#':
                    field[nr][nc] = field[r][c] + 1
                    queue.append((nr,nc, 'S'))
    return 'IMPOSSIBLE'
for _ in range(N):
    w, h = map(int, sys.stdin.readline().split())
    field = []

    fire = []
    sangeun = []
    for r in range(h):
        row = list(sys.stdin.readline().strip())
        for c in range(w):
            if row[c] == '@':
                sangeun.append([r,c])
            if row[c] == '*':
                fire.append([r,c])
        field.append(row)

    dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    queue = deque()
    queue.append([sangeun[0][0], sangeun[0][1], 'S'])
    field[sangeun[0][0]][sangeun[0][1]] = 0
    for r, c in fire:
        queue.append([r,c,'F'])
        field[r][c] = '#'

    print(bfs())