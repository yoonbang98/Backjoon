def solution(brown, yellow):
    answer = []
    for y_r in range(1, yellow + 1):
        if yellow%y_r == 0 and y_r >= yellow//y_r:
            print(y_r, yellow//y_r)
            if brown == 2*y_r + 2*yellow//y_r + 4:
                return [y_r + 2, yellow//y_r + 2]
    return answer