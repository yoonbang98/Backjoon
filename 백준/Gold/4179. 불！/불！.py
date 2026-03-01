import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
field = []

fire = []
jihun = []
for r in range(R):
    row = list(sys.stdin.readline().strip())
    for c in range(C):
        if row[c] == 'J':
            jihun.append([r,c])
        if row[c] == 'F':
            fire.append([r,c])
    field.append(row)

dir = [(1,0),(0,1),(0,-1),(-1,0)]

queue = deque()
queue.append((jihun[0][0], jihun[0][1], "J"))
field[jihun[0][0]][jihun[0][1]] = 0

for r,c in fire:
    queue.append((r,c,"F"))
    field[r][c] = "#"
def bfs():
    while queue:
        r,c,case = queue.popleft()
        if case == 'J' and (r == 0 or r == R-1 or c == 0 or c == C-1):
            if field[r][c] == '#':
                continue
            return field[r][c] + 1
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if field[nr][nc] != '#' and case == 'F':
                    field[nr][nc] = '#'
                    queue.append((nr,nc, 'F'))
                elif field[nr][nc] == '.' and case == 'J' and field[r][c] != '#':
                    field[nr][nc] = field[r][c] + 1
                    queue.append((nr,nc, 'J'))
    return 'IMPOSSIBLE'
print(bfs())