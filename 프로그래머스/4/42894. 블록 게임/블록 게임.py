from collections import defaultdict
def simulation(board, block_fill_loc):
    black_loc = []
    N = len(board)
    for c in range(N):
        for r in range(N):
            if board[r][c]:
                if r-1 >=0 :
                    black_loc.append([r-1,c])
                if r-2 >= 0 :
                    black_loc.append([r-2,c])
                break
    result = []
    for key, loc in block_fill_loc.items():
        if loc[0] in black_loc and loc[1] in black_loc:
            result.append(key)
    return result
def solution(board):
    N = len(board)
    block_loc = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if board[i][j] : block_loc[board[i][j]].append([i, j])
    block_fill_loc = defaultdict(list)
    for key, value in block_loc.items():
        row = [r for r, _ in value]
        col = [c for _, c in value]
        row_max, row_min = max(row), min(row)
        col_max, col_min = max(col), min(col)
        for r in range(row_min, row_max+1):
            for c in range(col_min, col_max+1):
                if board[r][c] != key:
                    block_fill_loc[key].append([r,c])
    answer = 0
    
    while True:
        result = simulation(board, block_fill_loc)
        if not result : break
        answer += len(result)
        for n in result:
            for r, c in block_loc[n]:
                board[r][c] = 0
            del block_loc[n]
            del block_fill_loc[n]
    return answer