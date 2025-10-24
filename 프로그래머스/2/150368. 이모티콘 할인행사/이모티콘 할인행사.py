from itertools import product
def solution(users, emoticons):
    answer = []
    for pro in product([10,20,30,40], repeat = len(emoticons)):
        result = [0, 0]
        for user_d_percent, user_price in users:
            price_tmp = 0
            for idx in range(len(emoticons)):
                if pro[idx] >= user_d_percent:
                    price_tmp += emoticons[idx]*(100-pro[idx])/100
            if price_tmp >= user_price:
                result[0] += 1
            else:
                result[1] += price_tmp
        answer.append(result)
    answer.sort(key = lambda x : (-x[0], -x[1]))           
    return answer[0]