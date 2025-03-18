from itertools import permutations
from collections import defaultdict, deque
import copy
from math import inf
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def minimum_key(board, src_r, src_c, dst_r, dst_c):
    dist = [[inf]*4 for _ in range(4)]
    dist[src_r][src_c] = 0
    queue = deque()
    queue.append([src_r, src_c, 0])
    while queue:
        cur_r, cur_c, cur_dist = queue.popleft()
        for dr, dc in dir:
            ctrl_r, ctrl_c = cur_r, cur_c
            while True:
                ctrl_nr, ctrl_nc = ctrl_r + dr, ctrl_c + dc
                if 0 > ctrl_nr or ctrl_nr >= 4 or 0 > ctrl_nc or ctrl_nc >= 4: break
                if 0 > ctrl_nr + dr or ctrl_nr + dr >= 4 or 0 > ctrl_nc + dc or ctrl_nc + dc >= 4:
                    if dist[ctrl_nr][ctrl_nc] > cur_dist + 1:
                        queue.append([ctrl_nr, ctrl_nc, cur_dist + 1])
                        dist[ctrl_nr][ctrl_nc] = cur_dist + 1
                    break
                if 0 <= ctrl_nr < 4 and 0 <= ctrl_nc < 4 and board[ctrl_nr][ctrl_nc]:
                    if dist[ctrl_nr][ctrl_nc] > cur_dist + 1:
                        dist[ctrl_nr][ctrl_nc] = cur_dist + 1
                        queue.append([ctrl_nr, ctrl_nc, cur_dist + 1])
                    break
                ctrl_r, ctrl_c = ctrl_nr, ctrl_nc
            nr, nc = cur_r + dr, cur_c + dc
            if 0 <= nr < 4 and 0 <= nc < 4 and dist[nr][nc] > cur_dist + 1:
                dist[nr][nc] = cur_dist + 1
                queue.append([nr, nc, cur_dist + 1])
    return dist[dst_r][dst_c]
                    
                
def solution(board, r, c):
    card_loc = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_loc[board[i][j]].append([i,j])
    card_num = len(card_loc.keys())
    answer = 1e7
    for per in permutations([i for i in range(1, card_num+1)], card_num):
        board_copy = copy.deepcopy(board)
        sr, sc = r, c
        result = 0
        for num in per:
            loc1, loc2 = card_loc[num][0], card_loc[num][1]

            loc1_key_num = minimum_key(board_copy, sr, sc, loc1[0], loc1[1])
            loc2_key_num = minimum_key(board_copy, sr, sc, loc2[0], loc2[1])
            if loc1_key_num < loc2_key_num :
                result += loc1_key_num
                board_copy[loc1[0]][loc1[1]] = 0
                next_key_num = minimum_key(board_copy, loc1[0], loc1[1], loc2[0], loc2[1])
                result += next_key_num
                board_copy[loc2[0]][loc2[1]] = 0
                sr, sc = loc2[0], loc2[1]
            else:
                result += loc2_key_num
                board_copy[loc2[0]][loc2[1]] = 0
                next_key_num = minimum_key(board_copy, loc2[0], loc2[1], loc1[0], loc1[1])
                result += next_key_num
                board_copy[loc1[0]][loc1[1]] = 0
                sr, sc = loc1[0], loc1[1]
            #print(num, result)
        answer = min(answer, result+card_num*2)
    
    return answer