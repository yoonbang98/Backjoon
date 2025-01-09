import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    q = deque()
    q.append([a,''])
    visited = [False]*10001
    while q:
        number, command = q.popleft()
        if number == b:
            print(command)
            break
        d = (2*number)%10000
        if not visited[d]:
            q.append([d, command + 'D'])
        s = (number-1)%10000
        if not visited[s]:
            q.append([s, command + 'S'])
        l = number // 1000 + (number%1000)*10
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        r = number // 10 + (number % 10) * 1000
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])