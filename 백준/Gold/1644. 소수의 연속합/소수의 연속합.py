import math
import sys

n = int(sys.stdin.readline())
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
	if array[i] == True:	# i가 소수인 경우
    	# i를 제외한 i의 모든 배수를 지우기
		j = 2
		while i * j <= n:
			array[i * j] = False
			j += 1

#모든 소수 출력
prime = []
for i in range(2, n + 1):
	if array[i]:
		prime.append(i)
start, end, total, answer = 0, 0, 0, 0
while True:
	if total >= n :
		total -= prime[start]
		start += 1
	elif end == len(prime):
		break
	else :
		total += prime[end]
		end += 1
	if total == n:
		answer += 1
print(answer)