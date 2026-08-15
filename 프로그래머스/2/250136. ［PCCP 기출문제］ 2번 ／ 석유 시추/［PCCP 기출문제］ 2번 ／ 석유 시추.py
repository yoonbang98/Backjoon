from collections import deque, defaultdict
dir = [(1,0), (0,1),(0,-1),(-1,0)]
def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False]*m for _ in range(n)]
    size_dict = defaultdict(int)
    cnt = 1
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                queue = deque()
                queue.append([i,j, cnt])
                size = 1
                visited[i][j] = cnt
                while queue:
                    r, c, cur = queue.popleft()

                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 > nr or n <= nr or 0 > nc or m <= nc: continue
                        if visited[nr][nc] or not land[nr][nc] : continue
                        if visited[nr][nc] and not visited[nr][nc] != cur : continue
                        visited[nr][nc] = cur
                        queue.append([nr,nc, cur])
                        size += 1
                size_dict[cnt] = size
                cnt += 1
    answer = 0
    for j in range(m):
        result = set()
        for i in range(n):
            if visited[i][j] : 
                result.add(visited[i][j])
        tmp = 0
        for num in result:
            tmp += size_dict[num]
        answer = max(answer, tmp)
            
    return answer