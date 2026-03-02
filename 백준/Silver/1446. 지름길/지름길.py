import sys

# N: 지름길의 개수, D: 고속도로의 길이

N, D = map(int, sys.stdin.readline().split())

graph = []

for _ in range(N):

    src, dst, dist = map(int, sys.stdin.readline().split())

    # 1. 역주행 불가 (dst > D)

    # 2. 지름길이 아닌 경우 (dst - src <= dist)

    if dst > D or dst - src <= dist: 

        continue

    graph.append([src, dst, dist])

# 출발 지점 기준으로 오름차순 정렬

graph.sort()

M = len(graph)

# 최악의 경우: 지름길을 하나도 타지 않고 끝까지 걸어가는 거리

answer = D 

def dfs(result, idx, cur):

    global answer

    

    # 현재 위치(cur)에서 도착점(D)까지 남은 거리를 지름길 없이 걸어가는 경우를 계산하여 최솟값 갱신

    answer = min(answer, result + (D - cur))

    

    # 현재 인덱스 이후의 지름길들을 탐색

    for j in range(idx, M):

        # 다음 지름길의 출발 지점이 현재 내 위치보다 같거나 앞에 있다면 탈 수 있음

        if graph[j][0] >= cur:

            # result + (지름길 시작점까지 걸어가는 거리) + (지름길의 길이)

            next_result = result + (graph[j][0] - cur) + graph[j][2]

            # 해당 지름길의 도착점을 새로운 현재 위치로 잡고 재귀 호출

            dfs(next_result, j + 1, graph[j][1])

# 누적 이동거리 0, 탐색할 지름길 인덱스 0, 현재 위치 0에서 시작

dfs(0, 0, 0)

print(answer)

