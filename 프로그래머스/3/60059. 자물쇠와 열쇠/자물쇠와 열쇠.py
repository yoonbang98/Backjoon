import copy
def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    field = [[0]*3*N for _ in range(3*N)]
    for i in range(N, 2*N):
        field[i][N:2*N] = lock[i-N]
    for _ in range(4):
        key = list(map(list, zip(*key[::-1])))
        for i in range(N-M, 2*N):
            for j in range(N-M, 2*N):
                field_copy = copy.deepcopy(field)
                for ii in range(M):
                    for jj in range(M):
                        field_copy[i + ii][j + jj] += key[ii][jj]
                flag = True
                for ii in range(N, 2*N):
                    for jj in range(N, 2*N):
                        if field_copy[ii][jj] != 1:
                            flag = False
                            break
                    if not flag: break
                if flag : answer = True
            if answer : break
        if answer : break
    return answer