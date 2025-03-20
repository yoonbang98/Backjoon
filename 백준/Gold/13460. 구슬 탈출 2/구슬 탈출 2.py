from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
field = []
for i in range(N):
    field.append(list(input()))
    for j in range(M):
        if field[i][j] == 'R':
            rx, ry = i, j
        elif field[i][j] == 'B':
            bx, by = i, j
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append([rx, ry, bx, by])

    cnt = 0
    visited = []
    visited.append((rx, ry, bx, by))

    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if field[rx][ry] == 'O':
                return cnt
            for dr, dc in dir:
                nrx, nry = rx, ry
                while True:
                    nrx += dr
                    nry += dc
                    if field[nrx][nry] == '#':
                        nrx -= dr
                        nry -= dc
                        break
                    if field[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dr
                    nby += dc
                    if field[nbx][nby] == '#':
                        nbx -= dr
                        nby -= dc
                        break
                    if field[nbx][nby] == 'O':
                        break
                if field[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dr
                        nry -= dc
                    else:
                        nbx -= dr
                        nby -= dc
                if (nrx, nry, nbx, nby) not in visited: # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
        if cnt > 10:
            return -1
    return -1
answer = bfs(rx, ry, bx, by)
print(answer)