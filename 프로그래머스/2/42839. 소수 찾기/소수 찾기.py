from itertools import permutations
from collections import defaultdict
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
def solution(numbers):
    num = len(numbers)
    visited = defaultdict(int)
    answer = 0
    for n in range(1, num+1):
        for per in permutations(numbers, n):
            tmp = ''
            for letter in per:
                tmp += letter
            if int(tmp) > 1 and not visited[int(tmp)]:
                visited[int(tmp)] = 1
                if is_prime(int(tmp)):
                    print(int(tmp))
                    answer += 1
    return answer