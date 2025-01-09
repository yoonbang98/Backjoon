import sys
from collections import defaultdict
N = int(sys.stdin.readline())


def back_tracking(cnt):
    if cnt == len(word):
        print("".join(answer))
        return
    #print(visited)
    # 반복문을 통해 visited에 단어를 확인
    for k in visited:
        if visited[k]:
            visited[k] -= 1 # k를 사용할 것으로 -1
            answer.append(k) # answer에 더해준다.
            back_tracking(cnt + 1) # 백트래킹
            visited[k] += 1 # k를 사용안한 것으로 +1
            answer.pop() # answer에서 빼준다.

for _ in range(N):
    word = sorted(list(map(str, sys.stdin.readline().strip())))
    visited = defaultdict(int)

    for letter in word:
        visited[letter] += 1
    answer = []
    back_tracking(0)