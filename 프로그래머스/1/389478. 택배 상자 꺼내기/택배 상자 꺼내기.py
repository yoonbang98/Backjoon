def solution(n, w, num):
    board = []
    cur_num = 1
    row_cnt = 0
    while n >= cur_num:
        n_list = [i for i in range(cur_num,cur_num + w)]
        if num in n_list:
            r_idx = row_cnt
            if row_cnt % 2:
                c_idx = n_list[::-1].index(num)
            else:
                c_idx = n_list.index(num)
        if row_cnt % 2:
            board.append(n_list[::-1])
        else:
            board.append(n_list)
        row_cnt += 1
        cur_num += w
    print(board)
    answer = 0
    for i in range(r_idx, len(board)):
        if board[i][c_idx] <= n:
            answer += 1
    
    return answer