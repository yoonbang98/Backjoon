from collections import deque
def solution(commands):
    answer = []
    table = [[0]*51 for _ in range(51)]
    graph = [[[] for _ in range(51)] for _ in range(51)]
    for command in commands:
        
        s_command = command.split(' ')
        if s_command[0] == 'UPDATE':
            if len(s_command) == 4:
                r, c = int(s_command[1]), int(s_command[2])
                table[r][c] = s_command[3]
                if graph[r][c]:
                    visited = []
                    visited.append([r,c])
                    queue = deque()
                    queue.append([r,c])
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        table[cur_r][cur_c] = s_command[3]
                        for nr, nc in graph[cur_r][cur_c]:
                            if [nr, nc] not in visited:
                                queue.append([nr, nc])
                                visited.append([nr, nc])           
            else:
                for r in range(1, 51):
                    for c in range(1, 51):
                        if table[r][c] == s_command[1]:
                            table[r][c] = s_command[2]
        elif s_command[0] == 'MERGE':
            r1, c1, r2, c2 = int(s_command[1]), int(s_command[2]), int(s_command[3]), int(s_command[4])
            if (r1, c1) == (r2, c2) : continue
            if [r2, c2] not in graph[r1][c1]:
                graph[r1][c1].append([r2, c2])
            if [r1, c1] not in graph[r2][c2]:
                graph[r2][c2].append([r1, c1])
            if table[r1][c1]:
                table[r2][c2] = table[r1][c1]
                if graph[r2][c2]:
                    visited = []
                    visited.append([r2,c2])
                    queue = deque()
                    queue.append([r2,c2])
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        table[cur_r][cur_c] = table[r1][c1]
                        for nr, nc in graph[cur_r][cur_c]:
                            if [nr, nc] not in visited:
                                queue.append([nr, nc])
                                visited.append([nr, nc])
            if not table[r1][c1] and table[r2][c2]:
                table[r1][c1] = table[r2][c2]
                if graph[r1][c1]:
                    visited = []
                    visited.append([r1,c1])
                    queue = deque()
                    queue.append([r1,c1])
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        table[cur_r][cur_c] = table[r2][c2]
                        for nr, nc in graph[cur_r][cur_c]:
                            if [nr, nc] not in visited:
                                queue.append([nr, nc])
                                visited.append([nr, nc])
            # print(command)
            # print(table)
            
        elif s_command[0] == 'UNMERGE':
            r, c = int(s_command[1]), int(s_command[2])
            visited = []
            visited.append([r,c])
            queue = deque()
            queue.append([r,c])
            while queue:
                cur_r, cur_c = queue.popleft()
                if (cur_r, cur_c) != (r, c):
                    table[cur_r][cur_c] = 0
                for nr, nc in graph[cur_r][cur_c]:
                    if [nr, nc] not in visited:
                        queue.append([nr, nc])
                        visited.append([nr, nc])
                graph[cur_r][cur_c] = []
            # print(command)
            # print(table)

        else:
            r, c = int(s_command[1]), int(s_command[2])
            if table[r][c]:
                answer.append(table[r][c])
            else:
                answer.append('EMPTY')
        
    #print(table)
    return answer