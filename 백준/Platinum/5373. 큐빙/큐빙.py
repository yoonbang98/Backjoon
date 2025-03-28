import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    command = list(input().split())
    cube_U = [['w']*3 for _ in range(3)]
    cube_D = [['y']*3 for _ in range(3)]
    cube_F = [['r']*3 for _ in range(3)]
    cube_B = [['o']*3 for _ in range(3)]
    cube_L = [['g']*3 for _ in range(3)]
    cube_R = [['b']*3 for _ in range(3)]
    for cmd in command:
        if cmd[0] == 'L':
            if cmd[1] == '+':
                cube_L = list(map(list, zip(*cube_L[::-1])))
                tmp_U = [cube_U[i][0] for i in range(3)]
                tmp_F = [cube_F[i][0] for i in range(3)][::-1]
                tmp_D = [cube_D[i][2] for i in range(3)]
                tmp_B = [cube_B[i][2] for i in range(3)][::-1]
                for i in range(3):
                    cube_F[i][0] = tmp_U[i]
                    cube_D[i][2] = tmp_F[i]
                    cube_B[i][2] = tmp_D[i]
                    cube_U[i][0] = tmp_B[i]
            else:
                cube_L = list(map(list, zip(*cube_L)))[::-1]
                tmp_U = [cube_U[i][0] for i in range(3)][::-1]
                tmp_B = [cube_B[i][2] for i in range(3)]
                tmp_D = [cube_D[i][2] for i in range(3)][::-1]
                tmp_F = [cube_F[i][0] for i in range(3)]

                for i in range(3):
                    cube_B[i][2] = tmp_U[i]
                    cube_D[i][2] = tmp_B[i]
                    cube_F[i][0] = tmp_D[i]
                    cube_U[i][0] = tmp_F[i]
        if cmd[0] == 'R':
            if cmd[1] == '+':
                cube_R = list(map(list, zip(*cube_R[::-1])))
                tmp_U = [cube_U[i][2] for i in range(3)][::-1]
                tmp_B = [cube_B[i][0] for i in range(3)]
                tmp_D = [cube_D[i][0] for i in range(3)][::-1]
                tmp_F = [cube_F[i][2] for i in range(3)]

                for i in range(3):
                    cube_B[i][0] = tmp_U[i]
                    cube_D[i][0] = tmp_B[i]
                    cube_F[i][2] = tmp_D[i]
                    cube_U[i][2] = tmp_F[i]
            else:
                cube_R = list(map(list, zip(*cube_R)))[::-1]
                tmp_U = [cube_U[i][2] for i in range(3)]
                tmp_F = [cube_F[i][2] for i in range(3)][::-1]
                tmp_D = [cube_D[i][0] for i in range(3)]
                tmp_B = [cube_B[i][0] for i in range(3)][::-1]
                for i in range(3):
                    cube_F[i][2] = tmp_U[i]
                    cube_D[i][0] = tmp_F[i]
                    cube_B[i][0] = tmp_D[i]
                    cube_U[i][2] = tmp_B[i]
        if cmd[0] == 'U':
            tmp_B, tmp_R, tmp_F, tmp_L = cube_B[0], cube_R[0], cube_F[0], cube_L[0]
            if cmd[1] == '+':
                cube_U = list(map(list, zip(*cube_U[::-1])))
                cube_R[0], cube_F[0], cube_L[0], cube_B[0] = tmp_B, tmp_R, tmp_F, tmp_L
            else:
                cube_U = list(map(list, zip(*cube_U)))[::-1]
                cube_L[0], cube_F[0], cube_R[0], cube_B[0] = tmp_B, tmp_L, tmp_F, tmp_R
        if cmd[0] == 'D':
            tmp_B, tmp_R, tmp_F, tmp_L = cube_B[2], cube_R[2], cube_F[2], cube_L[2]
            if cmd[1] == '+':
                cube_D = list(map(list, zip(*cube_D[::-1])))
                cube_L[2], cube_F[2], cube_R[2], cube_B[2] = tmp_B, tmp_L, tmp_F, tmp_R
            else:
                cube_D = list(map(list, zip(*cube_D)))[::-1]
                cube_R[2], cube_F[2], cube_L[2], cube_B[2] = tmp_B, tmp_R, tmp_F, tmp_L
        if cmd[0] == 'F':
            if cmd[1] == '+':
                cube_F = list(map(list, zip(*cube_F[::-1])))
                tmp_U = cube_U[2][:]
                tmp_R = [cube_R[i][0] for i in range(3)]
                tmp_D = cube_D[2][:][::-1]
                tmp_L = [cube_L[i][2] for i in range(3)][::-1]
                for i in range(3):
                    cube_R[i][0] = tmp_U[i]
                    cube_D[2][i] = tmp_R[i]
                    cube_L[i][2] = tmp_D[i]
                    cube_U[2][i] = tmp_L[i]
            else:
                cube_F = list(map(list, zip(*cube_F)))[::-1]
                tmp_U = cube_U[2][:][::-1]
                tmp_L = [cube_L[i][2] for i in range(3)][::-1]
                tmp_D = cube_D[2][:]
                tmp_R = [cube_R[i][0] for i in range(3)]
                for i in range(3):
                    cube_L[i][2] = tmp_U[i]
                    cube_D[2][i] = tmp_L[i]
                    cube_R[i][0] = tmp_D[i]
                    cube_U[2][i] = tmp_R[i]
        if cmd[0] == 'B':
            if cmd[1] == '+':
                cube_B = list(map(list, zip(*cube_B[::-1])))
                tmp_U = cube_U[0][:][::-1]
                tmp_L = [cube_L[i][0] for i in range(3)][::-1]
                tmp_D = cube_D[0][:]
                tmp_R = [cube_R[i][2] for i in range(3)]
                for i in range(3):
                    cube_L[i][0] = tmp_U[i]
                    cube_D[0][i] = tmp_L[i]
                    cube_R[i][2] = tmp_D[i]
                    cube_U[0][i] = tmp_R[i]
            else:
                cube_B = list(map(list, zip(*cube_B)))[::-1]
                tmp_U = cube_U[0][:]
                tmp_R = [cube_R[i][2] for i in range(3)]
                tmp_D = cube_D[0][:][::-1]
                tmp_L = [cube_L[i][0] for i in range(3)][::-1]
                for i in range(3):
                    cube_R[i][2] = tmp_U[i]
                    cube_D[0][i] = tmp_R[i]
                    cube_L[i][0] = tmp_D[i]
                    cube_U[0][i] = tmp_L[i]
    for row in cube_U:
        result = ''
        for letter in row:
            result += letter
        print(result)