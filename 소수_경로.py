import sys
import math
from collections import deque

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n % i:
            return False
    return True
prime_num = [False]*10000
for num in range(1000,10000):
    if is_prime(num):
        prime_num[num] = True

def bfs(start):
    queue = deque()
    visited[start] = 0
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for i in range(4):
            str_n = str(cur)
            tmp = str(cur)[i]
            for j in range(1, 10):
                add_num = int(tmp) + j
                if add_num >= 10:
                    add_num -= 10
                next_num = int(str_n[:i] + str(add_num) + str_n[i + 1:])
                if visited[next_num] == -1 and prime_num[next_num]:
                    visited[next_num] = visited[cur] + 1
                    queue.append(next_num)
T = int(sys.stdin.readline())
for _ in range(T):
    src, dst = map(int, sys.stdin.readline().split())
    visited = [-1]*(10000)
    bfs(src)
    if visited[dst] == -1:
        print('Impossible')
    else:
        print(visited[dst])
