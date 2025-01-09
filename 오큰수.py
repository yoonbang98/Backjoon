import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGE= [-1]*N
stack = [0] # 0번 인덱스

for i in range(1, N):
    # 오큰수 : A[i]의 오른쪽에 있으면서 A[i]보다 큰 수 중 가장 왼쪽 값
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i] # 해당 인덱스 칸은 A[i]
    stack.append(i)
print(*NGE)