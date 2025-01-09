import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())

field = []
for _ in range(N):
	field.append(list(map(int, sys.stdin.readline().split())))
command = []
for _ in range(M):
	command.append(list(map(int, sys.stdin.readline().split())))
dir = [[],(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]


cloud_queue = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
copy_dir = [(-1,-1),(-1,1),(1,1),(1,-1)]
water_queue = deque()
for d,s in command:
	visited = [[False]*N for i in range(N)]
	dr, dc = dir[d]
	while cloud_queue:
		r, c = cloud_queue.popleft()
		r = (r + dr * s) % N
		c = (c + dc * s) % N
		field[r][c] += 1
		visited[r][c] = True
		water_queue.append((r,c))
	while water_queue:
		r,c = water_queue.popleft()
		cnt = 0
		for dr,dc in copy_dir:
			nr = r + dr
			nc = c + dc
			if 0 <= nr < N and 0 <= nc < N and field[nr][nc] > 0:
				cnt += 1
		field[r][c] += cnt
	answer = 0
	for i in range(N):
		for j in range(N):
			if field[i][j] >= 2 and not visited[i][j]:
				field[i][j] -= 2
				cloud_queue.append((i,j))
			answer += field[i][j]
print(answer)

