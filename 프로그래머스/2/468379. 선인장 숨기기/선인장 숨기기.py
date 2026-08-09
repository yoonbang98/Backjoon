
from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    time = [[INF] * n for _ in range(m)]
    for i, (r, c) in enumerate(drops):
        time[r][c] = i + 1

    # 가로 슬라이딩 최소
    row_min = [[0] * (n - w + 1) for _ in range(m)]

    for r in range(m):
        dq = deque()
        for c in range(n):

            while dq and time[r][dq[-1]] >= time[r][c]:
                dq.pop()

            dq.append(c)

            if dq[0] <= c - w:
                dq.popleft()

            if c >= w - 1:
                row_min[r][c - w + 1] = time[r][dq[0]]

    best = -1
    ans = (0, 0)

    # 세로 슬라이딩
    for c in range(n - w + 1):
        dq = deque()

        for r in range(m):

            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()

            dq.append(r)

            if dq[0] <= r - h:
                dq.popleft()

            if r >= h - 1:

                val = row_min[dq[0]][c]
                top = r - h + 1

                # 핵심 수정 (tie-breaking)
                if val > best or (val == best and (top, c) < ans):
                    best = val
                    ans = (top, c)

    return list(ans)
