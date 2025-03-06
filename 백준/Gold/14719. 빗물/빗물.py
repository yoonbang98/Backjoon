import sys

n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

result = 0

while left < right:

    # 왼쪽 포인터를 옮기며, 왼쪽 블록 중 최대 블록 개수를 업데이트
    left_max = max(left_max, height[left])
    # 오른쪽 포인터를 옮기며, 오른쪽 블록 중 최대 블록 개수를 업데이트
    right_max = max(right_max, height[right])

    # 왼쪽 최대 블록 개수보다 오른쪽 최대 블록 개수가 크거나 같다면
    if left_max < right_max:
        # 왼쪽 최대 블록 개수와 현재 블록 개수의 차이만큼 물 채우기
        result += left_max - height[left]
        # 왼쪽의 인덱스를 증가
        left += 1

    # 왼쪽 최대 블록 개수가 오른쪽 최대 블록 개수보다 크다면
    else:
        # 오른쪽 최대 블록 개수와 현재 블록 개수의 차이만큼 물 채우기
        result += right_max - height[right]
        # 오른쪽의 인덱스를 감소
        right -= 1

print(result)