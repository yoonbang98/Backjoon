import sys
import copy
N, B = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
matrix_copy = copy.deepcopy(matrix)
degree = 1

binary = []
while True :     #B를 2진수로 치환
    t = B%2
    if t == 1:
        B = (B-1)//2
    else: B = B//2
    binary.append(t)
    if B <= 1:
        binary.append(B)
        break
def mat_mul(matrix1, matrix2):
    new_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            row = matrix1[i]
            col = [r[j] for r in matrix2]
            tmp = 0
            for k in range(N):
                tmp += row[k]*col[k]
            new_matrix[i][j] = tmp
    return new_matrix
answer = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    answer[i][i] = 1
for i in range(len(binary)):
    if binary[i] == 1:
        answer = mat_mul(answer, matrix)
        answer = [[x % 1000 for x in row] for row in answer]
    matrix= mat_mul(matrix, matrix)
    matrix = [[x % 1000 for x in row] for row in matrix]

for row in answer:
    print(*row)