from collections import deque
def solution(game_board, table):
    blank_loc_total = []
    N = len(game_board)
    visited = [[False]*N for _ in range(N)]
    dir = [(1,0), (0,1),(-1,0),(0,-1)]
    for i in range(N):
        for j in range(N):
            if not game_board[i][j] and not visited[i][j]:
                blank_loc = []
                queue = deque()
                queue.append([i,j])
                visited[i][j] = True
                while queue:
                    r, c = queue.popleft()
                    blank_loc.append([r,c])
                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and not game_board[nr][nc] and not visited[nr][nc]:
                            queue.append([nr,nc])
                            visited[nr][nc] = True
                blank_loc_total.append(blank_loc)
    table_info = []
    visited = [[False]*N for _ in range(N)]
    dir = [(1,0), (0,1),(-1,0),(0,-1)]
    for i in range(N):
        for j in range(N):
            if table[i][j] and not visited[i][j]:
                blank_loc = []
                queue = deque()
                queue.append([i,j])
                visited[i][j] = True
                while queue:
                    r, c = queue.popleft()
                    blank_loc.append([r,c])
                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and table[nr][nc] and not visited[nr][nc]:
                            queue.append([nr,nc])
                            visited[nr][nc] = True
                table_info.append(blank_loc)
    block_info = [[0]*N for _ in range(N)]
    for block in table_info:
        for r, c in block:
            block_info[r][c] = len(block)

    field_total = []
    for blank_loc in blank_loc_total:
        max_r, min_r = max([r for r, _ in blank_loc]), min([r for r, _ in blank_loc])
        max_c, min_c = max([c for _, c in blank_loc]), min([c for _, c in blank_loc])
        H, W = max_r - min_r + 1, max_c - min_c + 1
        field = [[1]*W for _ in range(H)]
        for r, c in blank_loc:
            field[r-min_r][c-min_c] = 0
        field_total.append([field, len(blank_loc)])
    answer = 0

    for field, M in field_total:
        flag3 = True
        #print(field, answer, table, M)
        for _ in range(4):
            field = list(map(list, zip(*field[::-1])))
            H, W = len(field), len(field[0])
            flag2 = True
            for sr in range(N-H+1):
                for sc in range(N-W+1):
                    tmp_loc = []
                    flag = True
                    for r in range(H):
                        for c in range(W):
                            if field[r][c] + table[sr+r][sc+c] == 1:
                                if field[r][c] == 0 and table[sr+r][sc+c] == 1 and M == block_info[sr+r][sc+c]:
                                    tmp_loc.append([sr+r, sc+c])
                                elif field[r][c] == 0 and table[sr+r][sc+c] == 1 and M != block_info[sr+r][sc+c]:
                                    flag = False
                                    break
                            else: 
                                flag = False
                                break
                        if not flag:
                            break
                    if flag: 
                        for rr, cc in tmp_loc:
                            table[rr][cc] = 0
                        answer += len(tmp_loc)
                        flag2 = False
                        break
                if not flag2: 
                    flag3 = False
                    break
            if not flag3: break
    
    return answer