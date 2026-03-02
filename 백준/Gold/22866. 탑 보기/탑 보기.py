import sys
input = sys.stdin.readline

N = int(input())
building = list(map(int, input().split()))
MAX = 1e9   #---> 적합하지 않은 값으로 설정시 틀릴 수 있음에 유의
cnt = [0] * N
nearest = [MAX] * N

# i번째 빌딩 기준 왼쪽에 보이는 건물 찾기
stack = []
for i in range(N):
    while stack and building[stack[-1]] <= building[i]:
        stack.pop()
    cnt[i] += len(stack)

    if stack:
        nearest[i] = stack[-1]
    stack.append(i)

# i번째 빌딩 기준 오른쪽에 보이는 건물 찾기
stack = []
for i in range(N-1, -1, -1):
    while stack and building[stack[-1]] <= building[i]:
        stack.pop()
    cnt[i] += len(stack)

    if stack:
        if abs(i-stack[-1]) < abs(i - nearest[i]):
            nearest[i] = stack[-1]
    stack.append(i)


for i in range(N):
    if cnt[i] >= 1:
        print(cnt[i], nearest[i] + 1)
    else:
        print(cnt[i])
