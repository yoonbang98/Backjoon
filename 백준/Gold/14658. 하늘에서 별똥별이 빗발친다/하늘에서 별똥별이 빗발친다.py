import sys

N, M, L, K = map(int, sys.stdin.readline().split())
stars = []
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    stars.append([r,c])

bounce = 0
for starA in stars:
    for starB in stars:
        cnt = 0
        for starC in stars:
            if starA[0] <= starC[0] and starC[0] <= starA[0] + L and\
            starB[1] <= starC[1] and starC[1] <= starB[1] + L:
                cnt += 1
            if cnt > bounce:
                bounce = cnt
print(K-bounce)