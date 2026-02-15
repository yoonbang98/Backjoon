import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

X = list(map(int, sys.stdin.readline().split()))

def possible(n):
    if len(X) == 1:
        if X[0] - n <= 0 and X[0] + n >= N :
            return 1
        else:
            return 0
    else:
        for idx, x in enumerate(X):
            if idx == 0:
                if x - n > 0 :
                    return 0
            elif idx == len(X) - 1:
                if x + n < N :
                    return 0
            else:
                if x + n < X[idx + 1] - n :
                    return 0
        return 1
answer = 0
left, right = 1, N
while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)