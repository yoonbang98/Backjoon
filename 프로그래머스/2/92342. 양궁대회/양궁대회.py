def solution(n, info):

    def brut(n, lion, idx): # 남은 화살수, 과녁, 현재 idx
        nonlocal gap, answer

        if idx > 10: # 정지조건
            # 화살이 남은경우 마지막에 다쏜다고 가정
            if n > 0:
                lion[10] += n
            score_apeach = 0
            score_lion = 0
            # 점수 세기
            for idx in range(0,11):
                if lion[idx] > apeach[idx]:
                    score_lion += 10-idx
                elif apeach[idx]:
                    score_apeach += 10-idx

            if score_lion - score_apeach > gap:
                gap = score_lion - score_apeach
                answer = lion[:]

            # 낮은 점수를 많이 쏜 경우 정답 최신화
            elif score_lion - score_apeach == gap:
                for i in range(10,-1,-1):
                    if answer[i] < lion[i]:
                        answer = lion[:]
                        break
                    elif answer[i] > lion[i]:
                        break
            lion[10] -= n
            return

        # 이번 idx(점수) 어피치를 이기는 경우와 지는경우 모두 탐색
        ## 이기는 경우
        if apeach[idx] + 1 <= n:
            lion[idx] = apeach[idx] + 1
            brut(n-apeach[idx]-1, lion, idx+1)
            lion[idx] = 0
        ## 지는 경우
        brut(n, lion, idx+1)

    apeach = info
    lion = [0] * 11
    gap = 1
    answer = []
    brut(n, lion, 0)

    return answer if answer else [-1]