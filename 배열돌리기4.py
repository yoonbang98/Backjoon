import sys
from collections import deque

N,M,K = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))
command = []
for _ in range(K):
    command.append(list(map(int, sys.stdin.readline().split())))

def turn(r,c,s,field):
    for i in range(s):
        queue = deque()
        queue.extend(field[r-s-1+i][c-s-1+i:c+s-1-i])
        queue.extend([row[c+s-1-i] for row in field[r-s-1+i:r+s-1-i]])
        queue.extend(field[r+s-1-i][c-s+i:c+s-i][::-1])
        queue.extend([row[c-s-1+i] for row in field[r-s+i:r+s-i][::-1]])

        queue.rotate(1)

        for j in range(c-s-1+i,c+s-1-i):
            field[r-s-1+i][j] = queue.popleft()
        for j in range(r-s-1+i,r+s-1-i):
            field[j][c+s-1-i] = queue.popleft()
        for j in range(c+s-i-1,c-s+i-1,-1):
            field[r+s-1-i][j] = queue.popleft()
        for j in range(r+s-i-1,r-s+i-1,-1 ):
            field[j][c-s-1+i] = queue.popleft()
    return field

def dfs(depth, field):
    global answer
    if depth == K:
        tmp = []
        for i in range(N):
            tmp.append(sum(field[i]))
        result = min(tmp)
        answer = min(answer, result)
        return
    for i in range(K):
        if not visited[i]:
            r,c,s = command[i]
            #idx.append(i)
            #field_prev = copy.deepcopy(field)
            new_field = turn(r,c,s,field)
            visited[i] = True
            dfs(depth+1, new_field)
            #field = field_prev
            visited[i] = False
answer = 1e9
visited = [False]*K
dfs(0,field)
print(answer)