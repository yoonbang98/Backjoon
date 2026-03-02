import sys

N = int(sys.stdin.readline())
a = sys.stdin.readline().strip()

red = a.count('R')
blue = N - red
answer = min(red, blue)

cnt = 0

for i in range(N):
    if a[i] != a[0]:
        break
    else:
        cnt += 1
if a[0] == 'R':
    answer = min(answer, red - cnt)
else:
    answer = min(answer, blue - cnt)

cnt = 0
for i in range(N-1, -1, -1):
    if a[i] != a[N-1]:
        break
    else :
        cnt += 1
if a[N-1] == 'R':
    answer = min(answer, red - cnt)
else:
    answer = min(answer, blue - cnt)
print(answer)