import sys

N = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))

answer = [0]
stack = [[1, top_list[0]]]

for i in range(1, len(top_list)):
    while stack:
        if stack[-1][1] >= top_list[i]:
            answer.append(stack[-1][0])
            stack.append([i+1, top_list[i]])
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
        stack.append([i+1, top_list[i]])
print(*answer)