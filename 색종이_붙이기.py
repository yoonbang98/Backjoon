import sys
board = []
for _ in range(10):
    board.append(list(map(int, sys.stdin.readline().split())))
color_paper = [5,5,5,5,5]

answer = 1e9
def attach_and_detach(r,c,s,v):
    for row in range(r, r+s+1):
        for col in range(c, c+s+1):
            board[row][col] = v
def possible_attach(r,c):
    s_list = []
    for size in range(5):
        if color_paper[size] and r + size < 10 and c + size < 10:
            flag = True
            for rr in range(r, r + size + 1):
                for cc in range(c, c + size + 1):
                    if board[rr][cc] == 0:
                        flag = False
                        break
            if flag:
                s_list.append(size)
    return s_list
def dfs(result):
    global answer
    for r in range(10):
        for c in range(10):
            if board[r][c]:
                s_list = possible_attach(r,c)
                for s in s_list:
                    attach_and_detach(r,c,s,0)
                    color_paper[s] -= 1
                    dfs(result + 1)
                    attach_and_detach(r,c,s,1)
                    color_paper[s] += 1
                return
    answer = min(answer, result)

dfs(0)
if answer == 1e9:
    print(-1)
else:
    print(answer)
