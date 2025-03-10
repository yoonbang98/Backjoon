from collections import deque

def get_next_pos(pos, board):
    n = len(board)
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 가로, 세로와 무관하게, 현재 로봇이 놓여져있는 상태에서 상하좌우로 이동할 수 있는지 탐색
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 해당 단계에선 이동하고자 하는 두 칸이 모두 비어 있는지(벽이 아닌지)만 판단
        if 0 <= pos1_next_x < n and  0 <= pos2_next_x < n and 0 <= pos1_next_y < n and 0 <= pos2_next_y < n:
            if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
                next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 현재 로봇이 가로로 놓여 있는 경우, 세로로도 회전할 수 있는지 추가적으로 탐색
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if 0 <= pos1_x+i < n and  0 <= pos2_x+i < n:
                if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                    # 왼쪽 칸을 기준으로 위, 아래로 회전
                    next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                    # 오른쪽 칸을 기준으로 위, 아래로 회전
                    next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 현재 로봇이 세로로 놓여 있는 경우, 가로로도 회전할 수 있는지 추가적으로 탐색
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if 0 <= pos1_y+i < n and  0 <= pos2_y+i < n:
                if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                    # 위 칸을 기준으로 왼쪽, 오른쪽으로 회전
                    next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                    # 아래 칸을 기준으로 왼쪽, 오른쪽으로 회전
                    next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 현재 위치에서 이동할 수 있는 모든 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)

    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(0, 0), (0, 1)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n-1, n-1) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0