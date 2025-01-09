import sys
sys.setrecursionlimit(10**8)
num_list = list(map(int, sys.stdin.readline().split()))

graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]
def dfs(depth, result, horse_list):
    global answer
    if depth == 10:
        answer = max(answer, result)
        return

    for i in range(4):
        horse = horse_list[i]
        if len(graph[horse]) == 2: #분기점이면
            horse = graph[horse][1]
        else :
            horse = graph[horse][0]
        for _ in range(1, num_list[depth]):
            horse = graph[horse][0]

        if horse == 32 or (horse < 32 and horse not in horse_list):
            prev = horse_list[i]
            horse_list[i] = horse

            dfs(depth+1, result+score[horse], horse_list)

            horse_list[i] = prev

answer = 0
horse_list = [0,0,0,0]
dfs(0,0,[0,0,0,0])
print(answer)
