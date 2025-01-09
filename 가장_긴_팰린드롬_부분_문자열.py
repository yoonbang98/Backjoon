import sys

# string = sys.stdin.readline()
# def expand(left, right):
#     while left >= 0 and right < len(string) and string[left] == string[right]:
#         left -= 1
#         right += 1
#         #print(string[left+1:right])
#     return len(string[left+1:right])
# if len(string) < 2 or string == string[::-1]:
#     print(len(string))
# else :
#     answer = 0
#     for i in range(len(string)-1):
#         answer = max(answer, expand(i,i+1), expand(i,i+2))
#     print(answer)

def manachers(S, N):
    A = [0] * N
    r, p = 0, 0
    for i in range(N):
        print(A)
        if i <= r:
            A[i] = min(A[2 * p - i], r - i)
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and S[i - A[i] - 1] == S[i + A[i] + 1]:
            A[i] += 1
        if r < i + A[i]:
            r = i + A[i]
            p = i
    return A

S = "#"+"#".join(sys.stdin.readline())+"#"
N = len(S)
A = manachers(S, N)
print(max(A))
