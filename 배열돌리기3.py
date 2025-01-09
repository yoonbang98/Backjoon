import sys

N,M,R = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
r_list = list(map(int, sys.stdin.readline().split()))
def rotate(command, array):
    global N, M
    if command == 1:
        return array[::-1]
    elif command == 2:
        tmp = []
        for row in array:
            tmp.append(row[::-1])
        return tmp
    elif command == 3:
        N, M = M, N
        return list(map(list, zip(*array[::-1])))
    elif command == 4:
        N, M = M, N
        return list(map(list, zip(*array)))[::-1]
    elif command == 5:
        tmp = [[0] * M for _ in range(N)]
        for i in range(N // 2):
            for j in range(M // 2):
                tmp[i][j] = array[i + N // 2][j]  # 4 -> 1
                tmp[i][j + M // 2] = array[i][j]  # 1 -> 2
                tmp[i + N // 2][j + M // 2] = array[i][j + M // 2]  # 2 -> 3
                tmp[i + N // 2][j] = array[i + N // 2][j + M // 2]  # 3 -> 4
        return tmp
    else:
        tmp = [[0] * M for _ in range(N)]
        for i in range(N // 2):
            for j in range(M // 2):
                tmp[i + N // 2][j + M // 2] = array[i + N // 2][j]  # 4 -> 1
                tmp[i + N // 2][j] = array[i][j]  # 1 -> 4
                tmp[i][j] = array[i][j + M // 2]  # 2 -> 1
                tmp[i][j + M // 2] = array[i + N // 2][j + M // 2]  # 3 -> 2
        return tmp
for r in r_list:
    array = rotate(r,array)
for row in array:
    print(*row)
