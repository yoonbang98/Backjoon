from collections import deque

dir = [(1,0),(0,1),(-1,0),(0,-1)]
def solution(storage, requests):
    storage_2d = []
    for store in storage:
        storage_2d.append(list(store))
    N, M = len(storage), len(storage[0])
    is_outside_total = [[False]*M for _ in range(N)]
    answer = 0
    for re in requests:
        is_outside = [[False]*M for _ in range(N)]
        if len(re) == 1:
            for i in range(N):
                for j in range(M):
                    if storage_2d[i][j] != re : continue
                    
                    flag = False
                    for dr, dc in dir:
                        nr, nc = i + dr, j + dc
                        if 0 > nr or N <= nr or 0 > nc or M <= nc or is_outside_total[nr][nc] : 
                            flag = True
                            break
                    if flag : 
                        storage_2d[i][j] = '.'
                        is_outside[i][j] = True
                            
        else:
            char = re[0]
            for i in range(N):
                for j in range(M):
                    if storage_2d[i][j] != char: continue
                    storage_2d[i][j] = '.'
                    flag = False
                    for dr, dc in dir:
                        nr, nc = i + dr, j + dc
                        if 0 > nr or N <= nr or 0 > nc or M <= nc or is_outside_total[nr][nc] : 
                            flag = True
                            break
                    if flag : 
                        is_outside[i][j] = True
        visited = [[False]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if storage_2d[i][j] == '.' and not is_outside_total[i][j] and not visited[i][j]:
                    queue = deque()
                    queue.append([i, j])
                    route = []
                    visited[i][j] = True
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        route.append([cur_r, cur_c])
                        for dr, dc in dir:
                            nr, nc = cur_r + dr, cur_c + dc
                            if 0 > nr or N <= nr or 0 > nc or M <= nc : continue
                            if storage_2d[nr][nc] == '.' and not visited[nr][nc] and not is_outside_total[nr][nc]:
                                queue.append([nr,nc])
                                visited[nr][nc] = True
                    flag = False
                    for r, c in route:
                        if is_outside[r][c] or is_outside_total[r][c]:
                            flag = True
                            break
                    if flag:
                        for r, c in route:
                            is_outside[r][c] = True
    
        for i in range(N):
            for j in range(M):
                if is_outside[i][j]:
                    is_outside_total[i][j] = True

    for i in range(N):
        for j in range(M):
            if storage_2d[i][j] != '.':
                answer += 1
    
    return answer





