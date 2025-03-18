field = [list(map(int, input().split())) for _ in range(10)]
color_paper = [5]*5
N = 0
for i in range(10):
    for j in range(10):
        if field[i][j]:
            N += 1
answer = 1e9
visited = [[False]*10 for _ in range(10)]
def max_size(field, visited, i,j):
    for size in range(2, 6):
        for ii in range(i, i+size):
            for jj in range(j, j+size):
                if ii >= 10 or jj >= 10:
                    return size - 1
                if not field[ii][jj] or visited[ii][jj]:
                    return size - 1
    return 5
def dfs(paper_cnt, cnt):
    global answer
    if cnt == N:
        answer = min(answer, paper_cnt)
        return
    if paper_cnt >= answer:
        return
    #print(paper_cnt, answer, color_paper)
    for i in range(10):
        for j in range(10):
            if field[i][j] and not visited[i][j]:
                max_num = max_size(field, visited, i, j)
                for size in range(max_num, 0, -1):
                    if color_paper[size-1]:
                        for ii in range(i, i + size):
                            for jj in range(j, j+size):
                                visited[ii][jj] = True
                        color_paper[size-1] -= 1
                        dfs(paper_cnt + 1, cnt + size**2)
                        for ii in range(i, i + size):
                            for jj in range(j, j+size):
                                visited[ii][jj] = False
                        color_paper[size-1] += 1
                return
dfs(0,0)
if N == 0:
    print(0)
else:
    if answer == 1e9:
        print(-1)
    else:
        print(answer)