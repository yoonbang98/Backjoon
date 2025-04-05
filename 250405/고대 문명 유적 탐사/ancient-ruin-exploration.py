import sys
from collections import deque
input = sys.stdin.readline

K, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(5)]
wall_num = list(map(int, input().split()))
wall_num = deque(wall_num)
def explore(field):
    result = []
    for cen_r in range(1,4):
        for cen_c in range(1,4):
            field_copy = [row[:] for row in field]
            field_tmp = []
            for i in range(cen_r-1, cen_r + 2):
                field_tmp.append(field[i][cen_c-1:cen_c + 2])
            for t in range(3):
                field_tmp = list(map(list, zip(*field_tmp[::-1][:])))
                for r_idx, row in enumerate(field_tmp):
                    field_copy[cen_r-1+r_idx][cen_c-1:cen_c + 2] = row[:]
                jewel_loc = find_jewel(field_copy)
                if jewel_loc:
                    field_copy_copy = [row[:] for row in field_copy]
                    result.append([len(jewel_loc), t, cen_c, cen_r, jewel_loc, field_copy_copy])

    if result:
        result.sort(key = lambda x : (-x[0], x[1],x[2],x[3]))
        return result[0]
    return result
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def find_jewel(field):
    jewel_loc = []
    visited = [[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                tmp = []
                queue = deque()
                num = field[i][j]
                queue.append([i,j])
                tmp.append([i,j])
                visited[i][j] = True
                while queue:
                    cur_r, cur_c = queue.popleft()
                    for dr, dc in dir:
                        nr, nc = cur_r + dr, cur_c + dc
                        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5: continue
                        if not visited[nr][nc] and field[nr][nc] == num:
                            queue.append([nr,nc])
                            visited[nr][nc] = True
                            tmp.append([nr, nc])
                if len(tmp) >= 3:
                    for jr, jc in tmp:
                        jewel_loc.append([jr,jc])
    return jewel_loc


answer = []
for _ in range(K):
    answer_tmp = 0
    result = explore(field)

    if not result: break
    answer_tmp += result[0]
    jew_loc, field = result[4], result[5]
    jew_loc.sort(key = lambda x : (x[1], -x[0]))

    for jr, jc in jew_loc:
        num = wall_num.popleft()
        field[jr][jc] = num
    while True:
        jew_loc = find_jewel(field)
        if not jew_loc:
            break
        jew_loc.sort(key = lambda x : (x[1], -x[0]))
        answer_tmp += len(jew_loc)

        for jr, jc in jew_loc:
            num = wall_num.popleft()
            field[jr][jc] = num
    answer.append(answer_tmp)

print(*answer)