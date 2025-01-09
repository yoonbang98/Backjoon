import sys
sys.setrecursionlimit(10**6)


def backtracking(l):
    global ans
    if len(l) == len(s):
        if l == s:
            ans = 1
    if l and l[-1] == 'A':
        backtracking(l[:-1])
    elif l and l[-1] == 'B':
        temp = l[:-1]
        backtracking(temp[::-1])


s = input()
t = input()
ans = 0

backtracking(t)
print(ans)
