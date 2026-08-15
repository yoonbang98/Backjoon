from itertools import product
dir = [(1,0), (0,1), (-1,0), (0,-1)]
def solution(maze):
    n, m = len(maze), len(maze[0])
    red_r, red_c, blue_r, blue_c, red_dst_r, red_dst_c, blue_dst_r, blue_dst_c = -1,-1,-1, -1,-1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1 : red_r, red_c = i, j
            if maze[i][j] == 2 : blue_r, blue_c = i, j
            if maze[i][j] == 3 : red_dst_r, red_dst_c = i, j
            if maze[i][j] == 4 : blue_dst_r, blue_dst_c = i, j
    red_visited = [[False]*m for _ in range(n)]
    blue_visited = [[False]*m for _ in range(n)]
    red_visited[red_r][red_c] = True
    blue_visited[blue_r][blue_c] = True
    
    answer = 1e9
    def dfs(depth, red_r, red_c, blue_r, blue_c, red_visited, blue_visited, maze):
        nonlocal answer
        if (red_r, red_c) == (red_dst_r, red_dst_c) and (blue_r, blue_c) == (blue_dst_r, blue_dst_c) : # 모두 도착한 경우
            answer = min(answer, depth)
            return
        red_flag, blue_flag = False, False
        if (red_r, red_c) == (red_dst_r, red_dst_c) : red_flag = True
        if (blue_r, blue_c) == (blue_dst_r, blue_dst_c) : blue_flag = True
        red_nxt = []
        for dr, dc in dir:
            nr, nc = red_r + dr, red_c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m : continue
            if red_visited[nr][nc] or maze[nr][nc] == 5: continue
            red_nxt.append([nr, nc])
        if not red_flag and not red_nxt : return
        blue_nxt = []
        for dr, dc in dir:
            nr, nc = blue_r + dr, blue_c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m : continue
            if blue_visited[nr][nc] or maze[nr][nc] == 5: continue
            blue_nxt.append([nr, nc])
        if not blue_flag and not blue_nxt : return
    
        if red_flag : #red만 도착
            for blue_nxt_r, blue_nxt_c in blue_nxt:
                if (blue_nxt_r, blue_nxt_c) == (red_r, red_c): continue
                blue_visited[blue_nxt_r][blue_nxt_c] = True
                dfs(depth + 1, red_r, red_c, blue_nxt_r, blue_nxt_c, red_visited, blue_visited, maze)
                blue_visited[blue_nxt_r][blue_nxt_c] = False
        elif blue_flag : 
            for red_nxt_r, red_nxt_c in red_nxt:
                if (red_nxt_r, red_nxt_c) == (blue_r, blue_c): continue
                red_visited[red_nxt_r][red_nxt_c] = True
                dfs(depth + 1, red_nxt_r, red_nxt_c, blue_r, blue_c, red_visited, blue_visited, maze)
                red_visited[red_nxt_r][red_nxt_c] = False
        else : # 둘 다 도착 x
            for prod in product(red_nxt, blue_nxt):
                red_nxt_r, red_nxt_c = prod[0]
                blue_nxt_r, blue_nxt_c = prod[1]
                if (red_nxt_r, red_nxt_c) == (blue_r, blue_c) and (blue_nxt_r, blue_nxt_c) == (red_r, red_c) : continue
                if (red_nxt_r, red_nxt_c) == (blue_nxt_r, blue_nxt_c) : continue
                red_visited[red_nxt_r][red_nxt_c] = True
                blue_visited[blue_nxt_r][blue_nxt_c] = True
                dfs(depth + 1, red_nxt_r, red_nxt_c, blue_nxt_r, blue_nxt_c, red_visited, blue_visited, maze)
                red_visited[red_nxt_r][red_nxt_c] = False
                blue_visited[blue_nxt_r][blue_nxt_c] = False
        return
    dfs(0, red_r, red_c, blue_r, blue_c, red_visited, blue_visited, maze)
        
    if answer == 1e9 : return 0
    return answer