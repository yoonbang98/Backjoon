from collections import deque

dir = [(1,0),(-1,0),(0,1),(0,-1)]


def solution(game_board, table):
    answer = 0
    N = len(table)
    visited = [[-1]*N for _ in range(N)]
    block_list = []
    for i in range(N):
        for j in range(N):
            if table[i][j] and visited[i][j] == -1:
                queue = deque()
                queue.append([i,j])
                visited[i][j] = True
                block = []
                while queue:
                    cur_r, cur_c = queue.popleft()
                    block.append([cur_r, cur_c])
                    for dr, dc in dir:
                        nr, nc = cur_r + dr, cur_c + dc
                        if 0 > nr or 0 > nc or N <= nc or N <= nr: continue
                        if visited[nr][nc] == -1 and table[nr][nc] == 1:
                            visited[nr][nc] = True
                            queue.append([nr, nc])
                num = len(block)
                min_r, max_r = min([r for r, _ in block]), max([r for r, _ in block])
                min_c, max_c = min([c for _, c in block]), max([c for _, c in block])
                tmp = []
                for r in range(min_r, max_r + 1):
                    tmp.append(table[r][min_c:max_c + 1])
                block_list.append([tmp, num])
    visited = [[-1]*N for _ in range(N)]
    blank_list = []
    for i in range(N):
        for j in range(N):
            if not game_board[i][j] and visited[i][j] == -1:
                queue = deque()
                queue.append([i,j])
                visited[i][j] = True
                block = []
                while queue:
                    cur_r, cur_c = queue.popleft()
                    block.append([cur_r, cur_c])
                    for dr, dc in dir:
                        nr, nc = cur_r + dr, cur_c + dc
                        if 0 > nr or 0 > nc or N <= nc or N <= nr: continue
                        if visited[nr][nc] == -1 and not game_board[nr][nc]:
                            visited[nr][nc] = True
                            queue.append([nr, nc])
                num = len(block)
                min_r, max_r = min([r for r, _ in block]), max([r for r, _ in block])
                min_c, max_c = min([c for _, c in block]), max([c for _, c in block])
                tmp = []
                for r in range(min_r, max_r + 1):
                    tmp.append(game_board[r][min_c:max_c + 1])
                blank_list.append([tmp, num])
    visited2 = [False]*len(block_list)
    for blank, blank_num in blank_list:
        flag = False
        for idx, (block, block_num) in enumerate(block_list):
            if flag : break
            if not visited2[idx] and blank_num == block_num:
                for _ in range(4):
                    if flag : break
                    block = list(map(list, zip(*block[::-1])))
                    if len(block) == len(blank) and len(block[0]) == len(blank[0]):
                        flag2 = True
                        for r in range(len(block)):
                            for c in range(len(block[0])):
                                if not block[r][c] + blank[r][c] == 1:
                                    flag2 = False
                                    break
                            if not flag2 : break
                        if flag2 : 
                            flag = True
                            visited2[idx] = True
                    else:
                        continue
    for idx, v in enumerate(visited2):
        if v :
            answer += block_list[idx][1]
            
    return answer