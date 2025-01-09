import sys
from collections import deque
import copy

dir = [(0,1),(1,0),(0,-1),(-1,0)]
N, Q = map(int, sys.stdin.readline().split())
field = []
for i in range(2**N):
    field.append(list(map(int, sys.stdin.readline().split())))
L_list = list(map(int, sys.stdin.readline().split()))
NN = len(field)

def rotate(array):
    length = len(array)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            temp[i][j] = array[length - 1 - j][i]
    return temp
def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    global visited
    visited[i][j] = True
    ice = 1
    while queue:
        r,c = queue.popleft()
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < NN and 0 <= nc < NN and field[nr][nc] > 0 and not visited[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = True
                ice += 1
    return ice
for l in L_list:
    sub = 2**l
    if l > 0:
        for i in range(int(NN/sub)):
            i_s = i*sub
            i_e = i*sub + sub
            sub_field = field[i_s:i_e]
            for j in range(int(NN/sub)):
                j_s = j * sub
                j_e = j * sub + sub
                sub_sub = [col[j_s:j_e] for col in sub_field]
                sub_sub = list(map(list, zip(*sub_sub[::-1])))
                i_tmp = 0
                for ii in range(i_s,i_e):
                    j_tmp = 0
                    for jj in range(j_s,j_e):
                        field[ii][jj] = sub_sub[i_tmp][j_tmp]
                        j_tmp+=1
                    i_tmp+=1
    tmp = [[0]*NN for _ in range(NN)]
    #print(field)
    for r in range(NN):
        for c in range(NN):
            if field[r][c] > 0:
                near = 0
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < NN and 0 <= nc < NN and field[nr][nc] > 0:
                        near += 1
                if near < 3:
                    tmp[r][c] = field[r][c] - 1
                else :
                    tmp[r][c] = field[r][c]
            else :
                tmp[r][c] = 0
    field = copy.deepcopy(tmp)
    #print(field)

visited = [[False]*NN for _ in range(NN)]
cnt = 0
max_ice = 0
for i in range(NN):
    for j in range(NN):
        if field[i][j] > 0 :
            cnt += field[i][j]
            if not visited[i][j]:
                ice = bfs(i,j)
                if max_ice <= ice :
                    max_ice = ice

print(cnt)
print(max_ice)
