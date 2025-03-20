from math import inf
N = int(input())
feature = list(map(int, input().split()))

answer = inf
left = 0
right = N-1
answer_list = [feature[left], feature[right]]
while left < right:
    result = feature[left] + feature[right]
    if answer > abs(result): #작아지면
        answer = abs(result)
        answer_list = [feature[left], feature[right]]
    if result > 0:
        right -= 1
    else:
        left += 1
print(*answer_list)