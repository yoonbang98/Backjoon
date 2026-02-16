import sys
from collections import defaultdict

room_total = []
P, M = map(int, sys.stdin.readline().split())
room_cnt = 1
for _ in range(P):
    L, N = sys.stdin.readline().strip().split()
    L = int(L)
    if not room_total:
        room = defaultdict(int)
        room[N] = L
        room_total.append([room_cnt, L,room])
        room_cnt += 1
    else:
        flag = False
        for idx, (room_cnt, thres, room) in enumerate(room_total):
            if flag : break
            if len(room.values()) < M and thres - 10 <= L <= thres + 10:
                room[N] = L
                flag = True
                room_total[idx] = [room_cnt, thres, room]
        if not flag:
            room = defaultdict(int)
            room[N] = L
            room_total.append([room_cnt, L,room])
            room_cnt += 1
for room_cnt, _, room in room_total:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    sorted_room = sorted(room.items(), key = lambda x : x[0])
    for key, value in sorted_room:
        print(value, key)