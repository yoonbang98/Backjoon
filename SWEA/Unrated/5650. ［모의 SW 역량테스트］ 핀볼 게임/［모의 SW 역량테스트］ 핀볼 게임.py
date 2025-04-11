# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dir = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
next_d = {3 : [[2,0],[2,0],[1,1],[0,1],[2,0]], 1: [[3,1],[0,0],[0,0],[2,1],[0,0]], 0 : [[1,0],[3,1],[2,1],[1,0],[1,0]], 2 : [[0,1],[1,1],[3,0],[3,0],[3,0]]}
def simulation(sr, sc, d):
    result = 0
    r, c, cur_d = sr, sc, d
    while True:
        nr, nc = r + dir[cur_d][0], c + dir[cur_d][1]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: #벽
            result += 1
            if cur_d%2 == 0:
                cur_d += 1
            else:
                cur_d -= 1
            if 1 <= field[r][c] <= 4: #블록
                result += 1
                cur_d, move_flag = next_d[cur_d][field[r][c] - 1]
            elif 6 <= field[r][c] <= 10:
                warm_loc = warm_hall[field[r][c]]
                for wr, wc in warm_loc:
                    if (wr, wc) != (r, c):
                        nnr, nnc = wr, wc
                r, c = nnr, nnc
            else:
                pass
        else: #안
            if not field[nr][nc]: # 빈칸일 때
                r, c = nr, nc
            else:
                if 1 <= field[nr][nc] <= 5: #블록
                    result += 1
                    cur_d, move_flag = next_d[cur_d][field[nr][nc] - 1]
                    if move_flag:
                        r, c = nr, nc
                    else:
                        if 1 <= field[r][c] <= 4: #블록
                            result += 1
                            cur_d, move_flag = next_d[cur_d][field[r][c] - 1]
                        elif 6 <= field[r][c] <= 10:
                            warm_loc = warm_hall[field[r][c]]
                            for wr, wc in warm_loc:
                                if (wr, wc) != (r, c):
                                    nnr, nnc = wr, wc
                            r, c = nnr, nnc
                        else:
                            pass
                if 6 <= field[nr][nc] <= 10:
                    warm_loc = warm_hall[field[nr][nc]]
                    for wr, wc in warm_loc:
                        if (wr, wc) != (nr, nc):
                            nnr, nnc = wr, wc
                    r, c = nnr, nnc
                if field[nr][nc] == -1:
                    return result
        if (r, c) == (sr, sc):
            return result
    return result

for test_case in range(1, T + 1):
    warm_hall = defaultdict(list)
    field = []
    N = int(input())
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if 6 <= row[c] <= 10:
                warm_hall[row[c]].append([r,c])
        field.append(row)
    answer = 0

    for sr in range(N):
        for sc in range(N):
            if not field[sr][sc]:
                for d in range(4):
                    result = simulation(sr,sc,d)
                    #print(sr, sc, d, result)
                    answer = max(result, answer)
    print('#{} {}'.format(test_case, answer))
