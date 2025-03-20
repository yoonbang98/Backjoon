N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
answer = 0

for idx, num in enumerate(num_list):
    left, right = 0, N-1
    while left < right:
        if left == idx:
            left += 1
            continue
        if right == idx:
            right -= 1
            continue
        result = num_list[left] + num_list[right]
        if result <= num :
            if result == num:
                answer += 1
                break
            left += 1
        else:
            right -= 1
print(answer)