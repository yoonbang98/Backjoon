import sys
N = int(sys.stdin.readline())
building = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        if i == j : continue
        elif abs(j - i) == 1:
            tmp += 1
            continue
        else:
            slope = (building[i]-building[j]) / (i-j)
            intercept = -1*slope*i + building[i]
            flag = True
            if i > j:
                for middle in range(j+1, i):
                    if slope*middle + intercept <= building[middle]:
                        flag = False
                        break
            else:
                for middle in range(i + 1, j):
                    if slope*middle + intercept <= building[middle]:
                        flag = False
                        break
            if flag : tmp += 1
    answer = max(answer, tmp)
print(answer)