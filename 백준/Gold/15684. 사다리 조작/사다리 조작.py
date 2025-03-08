import sys

N, M, H = map(int, sys.stdin.readline().split())
sadari = [[0] * (N-1) for _ in range(H)]

# 사다리 입력 받기
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    sadari[a-1][b-1] = 1  # 가로선 표시

def sadari_game():
    """현재 사다리에서 모든 출발점이 자기 번호로 도착하는지 확인"""
    for start in range(N):
        cur = start
        for h in range(H):
            if cur < N-1 and sadari[h][cur] == 1:  # 오른쪽으로 이동
                cur += 1
            elif cur > 0 and sadari[h][cur-1] == 1:  # 왼쪽으로 이동
                cur -= 1
        if cur != start:  # 자기 번호로 도착하지 못하면 실패
            return False
    return True

def dfs(cnt, x, y):
    global answer
    if cnt >= answer:  # 가지치기 (이미 찾은 최소 개수보다 많다면 중단)
        return
    if sadari_game():  # 현재 사다리가 조건을 만족하면 최소 개수 갱신
        answer = min(answer, cnt)
        return
    if cnt == 3:  # 3개 이상 추가하면 무조건 종료
        return

    # 가로선 추가 시도 (위에서 아래로, 왼쪽에서 오른쪽으로 탐색)
    for i in range(x, H):
        for j in range(y if i == x else 0, N-1):  # 같은 줄에서는 y 이후부터 탐색
            if sadari[i][j] == 0 and (j == 0 or sadari[i][j-1] == 0) and (j == N-2 or sadari[i][j+1] == 0):
                sadari[i][j] = 1  # 가로선 추가
                dfs(cnt + 1, i, j + 2)  # 연속 가로선 방지: 다음 탐색은 j+2부터
                sadari[i][j] = 0  # 원상 복구

answer = 4  # 최대로 놓을 수 있는 가로선 개수는 3개
if sadari_game():
    print(0)
else:
    dfs(0, 0, 0)
    print(answer if answer < 4 else -1)