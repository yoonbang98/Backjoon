import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [-1]*100001
visited[N] = 0

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        cur = queue.popleft()
        if cur == K:
            return
        if cur > 0:
            target = cur
            while True:
                if target*2 <= 100000 and visited[target*2] == -1:
                    queue.append(target*2)
                    visited[target*2] = visited[cur]
                    target *= 2
                else:
                    break
        if cur - 1 >= 0 and visited[cur-1] == -1:
            visited[cur-1] = visited[cur] + 1
            queue.append(cur-1)
        if cur + 1 <= 100000 and visited[cur+1] == -1 :
            visited[cur+1] = visited[cur] + 1
            queue.append(cur+1)
bfs(N)
print(visited[K])