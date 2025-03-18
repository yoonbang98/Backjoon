import sys
sys.setrecursionlimit(10000) # 재귀 허용깊이 임의로 지정

def solution(k, room_number):
    rooms = dict() # {방번호: 바로 다음 빈방 번호}
    for num in room_number:
        chk_in = find_emptyroom(num,rooms)
    return list(rooms.keys())

def find_emptyroom(chk, rooms):
    if chk not in rooms.keys():
        rooms[chk] = chk + 1
        return chk
    empty = find_emptyroom(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty
    