import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
answer = 0
visited = set()
start = 0
for end in range(N):
    while num_list[end] in visited:
        visited.remove(num_list[start])
        start += 1
    visited.add(num_list[end])
    answer += (end - start + 1)
print(answer)
