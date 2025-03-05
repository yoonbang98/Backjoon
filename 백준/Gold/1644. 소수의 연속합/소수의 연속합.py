from math import sqrt
N = int(input())
prime_list = []
def is_prime(n):
    for num in range(2, int(sqrt(n)) + 1):
        if n%num == 0:
            return False
    return True
for n in range(2, N+1):
    if is_prime(n):
        prime_list.append(n)
M = len(prime_list)
start, end = 0, 0
answer = 0
if not M :
    print(answer)
else:
    sum_tmp = prime_list[0]
    while start <= end:
        if sum_tmp <= N:
            if sum_tmp == N :
                answer += 1
            end += 1
            if end == M : break
            sum_tmp += prime_list[end]
        else :
            sum_tmp -= prime_list[start]
            start += 1
    print(answer)

