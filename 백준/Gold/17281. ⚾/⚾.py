from itertools import permutations
N = int(input())
inning_result = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for per in permutations([i for i in range(1,9)]):
    per = list(per)
    batter_idx = per[:3] + [0] + per[3:]
    result = 0
    p_num = 0
    inning_num = 0
    while inning_num < N:
        inning_tmp = inning_result[inning_num]
        b1, b2, b3 = 0,0,0
        out = 0
        while out < 3:
            if not inning_tmp[batter_idx[p_num]]:
                out += 1
                p_num = (p_num + 1)%9
                continue
            if 1 <= inning_tmp[batter_idx[p_num]] <= 3 : #안타, 2루타, 3루타
                if inning_tmp[batter_idx[p_num]]== 3:
                    result += (b1+b2+b3)
                    b1, b2, b3 = 0, 0, 1
                elif inning_tmp[batter_idx[p_num]] == 2:
                    result += (b2+b3)
                    b1, b2, b3 = 0, 1, b1
                else:
                    result += (b3)
                    b1, b2, b3 = 1, b1, b2
            if inning_tmp[batter_idx[p_num]] == 4 : #홈런
                result += (b1+b2+b3+1)
                b1, b2, b3 = 0, 0, 0
            p_num = (p_num + 1)%9
        inning_num += 1
    answer = max(answer, result)
print(answer)
