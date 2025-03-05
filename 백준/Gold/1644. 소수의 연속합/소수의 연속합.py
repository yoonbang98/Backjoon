import math
N = int(input())
primes = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N))+1):
    if primes[i] == True:
        j = 2
        while i*j <= N:
            primes[i*j] = False
            j += 1

prime_list = []

for i in range(2, N+1):
    if primes[i]:
        prime_list.append(i)

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
