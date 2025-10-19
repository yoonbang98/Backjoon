from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons, len(dungeons)):
        hp = k
        result = 0
        for min_hp, use_hp in per:
            if min_hp <= hp:
                hp -= use_hp
                result += 1
            else : break
        answer = max(answer , result)
    return answer