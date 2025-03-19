from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
j_r, j_c = -1, -1

fire_loc = []
for i in range(R):
    for j in range(C):
        if field[i][j] == 'J':
            j_r, j_c = i, j
        if field[i][j] == 'F':
            fire_loc.append([i,j])
answer = 1e9
dir = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[-1]*C for _ in range(R)]
visited[j_r][j_c] = 0
queue = deque()
queue.append([j_r, j_c, 0])
fire_queue = deque(fire_loc)

while True:
    nxt = []
    while queue:
        r,c, dist = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if field[r][c] == 'F': continue
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == -1 and field[nr][nc] =='.':
                visited[nr][nc] = dist + 1
                field[nr][nc] = 'J'
                nxt.append([nr,nc, visited[nr][nc]])
            if 0 > nr or R <= nr or 0 > nc or C <= nc:
                answer = dist + 1
                break
    queue = deque(nxt)
    if answer != 1e9:
        break
    if not queue:
        answer = -1
        break
    nxt_fire = []

    while fire_queue:
        fr, fc = fire_queue.popleft()
        for dr, dc in dir:
            f_nr, f_nc = dr + fr, dc + fc

            if 0 <= f_nr < R and 0 <= f_nc < C and (field[f_nr][f_nc] == 'J' or field[f_nr][f_nc] == '.'):
                field[f_nr][f_nc] = 'F'
                nxt_fire.append([f_nr, f_nc])
    fire_queue = deque(nxt_fire)

if answer == -1:
    print('IMPOSSIBLE')
else:
    print(answer)
