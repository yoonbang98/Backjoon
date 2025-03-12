from collections import deque

def solution(alp, cop, problems):
    # 목표 alp, cop 찾기
    max_alp, max_cop = alp, cop
    for a_req, c_req, _, _, _ in problems:
        max_alp = max(max_alp, a_req)
        max_cop = max(max_cop, c_req)
    
    # DP 테이블 초기화
    INF = float('inf')
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    # 문제 리스트에 기본 공부 방법 추가 (알고력 +1, 코딩력 +0) (코스트 1)
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    # BFS 탐색
    queue = deque([(alp, cop)])
    while queue:
        a, c = queue.popleft()

        for a_req, c_req, a_rwd, c_rwd, cost in problems:
            if a >= a_req and c >= c_req:  # 문제를 풀 수 있는 경우
                nxt_a, nxt_c = min(max_alp, a + a_rwd), min(max_cop, c + c_rwd)
                if dp[nxt_a][nxt_c] > dp[a][c] + cost:
                    dp[nxt_a][nxt_c] = dp[a][c] + cost
                    queue.append((nxt_a, nxt_c))

    return dp[max_alp][max_cop]