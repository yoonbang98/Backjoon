def solution(players, m, k):
    answer = 0
    cur = []
    for idx, player in enumerate(players):
        if cur:
            new_cur = []
            for c_idx, num in cur:
                if abs(c_idx - idx) < k:
                    new_cur.append([c_idx, num])
            cur = new_cur
        if player // m:
            if not cur :
                cur.append([idx, player//m])
                answer += player//m
            else:
                cnt = sum([i for _ , i in cur])
                if cnt < player//m:
                    cur.append([idx, player//m - cnt])
                    answer += player//m-cnt
        # print(idx, cur, answer)
        
                
    return answer