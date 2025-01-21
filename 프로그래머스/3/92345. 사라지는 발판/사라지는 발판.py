dir = [(1,0),(0,1),(-1,0),(0,-1)]
def get_next_loc(board, loc):
    R, C = len(board), len(board[0])
    cur_r, cur_c = loc[0], loc[1]
    possible_loc = []
    for dr, dc in dir:
        nr, nc = cur_r + dr, cur_c + dc
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc]:
            possible_loc.append([nr, nc])
    return possible_loc
        
def dfs(result, board, aloc, bloc):
    if result % 2 == 0 : # A 이동
        next_loc = get_next_loc(board, aloc)
    else : # B 이동
        next_loc = get_next_loc(board, bloc)
    if not next_loc :
        return result % 2 != 0, result # A 승리 시 True, B 승리 시 False
    if aloc == bloc :
        return (result+1) % 2 != 0, result + 1 # A 승리 시 True, B 승리 시 False
    win, lose = [], []
    if result % 2 == 0: # A 이동 차례
        board[aloc[0]][aloc[1]] = 0
        for nr, nc in next_loc:
            a_win, cnt = dfs(result + 1, board, [nr, nc], bloc)
            if a_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[aloc[0]][aloc[1]] = 1
    else: # B 이동
        board[bloc[0]][bloc[1]] = 0
        for nr, nc in next_loc:
            a_win, cnt = dfs(result+1, board, aloc, [nr, nc])
            if not a_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[bloc[0]][bloc[1]] = 1

    if win:                             # 승리하는 경우가 하나라도 있으면 
        return result % 2 == 0, min(win)  # 승리하는 사람과 가장 빨리 승리하는 경우를 반환한다.
    else:                               # 승리하는 경우가 하나도 없으면
        return result % 2 != 0, max(lose) # 패배하는 가장 긴 루트를 반환한다.

            
    
def solution(board, aloc, bloc):
    winner, answer = dfs(0, board, aloc, bloc)
    return answer