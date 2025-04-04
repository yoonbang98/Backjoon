def solution(board, skill):
    N, M = len(board), len(board[0])
    field = [[0]*(M+1) for _ in range(N+1)]

    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            field[r1][c1] -= d
            field[r2+1][c1] += d
            field[r1][c2+1] += d
            field[r2+1][c2+1] -= d
        else :
            field[r1][c1] += d
            field[r2+1][c1] -= d
            field[r1][c2+1] -= d
            field[r2+1][c2+1] += d

    for i in range(N+1):
        for j in range(1,M+1): # 왼쪽에서 오른쪽
            field[i][j] = field[i][j-1] + field[i][j]
    
    for j in range(M+1):
        for i in range(1,N+1): # 위에서 아래
            field[i][j] = field[i-1][j] + field[i][j]

    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] = board[i][j] + field[i][j]
            if board[i][j] > 0 :
                answer += 1
    return answer