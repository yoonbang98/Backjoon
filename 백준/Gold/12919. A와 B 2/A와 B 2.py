import sys
S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())
answer = 0
def dfs(s, t):
    global answer
    if len(s) == len(t):
        if s == t:
            answer = 1
        return
    if t[-1] == 'A':
        dfs(s, t[:-1])
    if t[0] == 'B':
        dfs(s, t[::-1][:-1])
dfs(S,T)
print(answer)