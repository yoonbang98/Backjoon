import sys
from collections import deque, defaultdict

s = sys.stdin.readline().strip()

def right(s):
    queue = deque()
    for ss in s:
        if ss == '(' or ss == '[':
            queue.append(ss)
        elif ss == ')':
            try :
                if queue.pop() == '(':
                    pass
                else :
                    return False
            except:
                return False
        elif ss ==']':
            try:
                if queue.pop() == '[':
                    pass
                else:
                    return False
            except:
                return False
    if len(queue):
        return False
    return True
if not right(s):
    print(0)
else:
    queue = deque()
    score = defaultdict(int)
    for ss in s:
        if ss == '(' or ss == '[':
            queue.append(ss)
        elif ss == ')':
            queue.pop()
            if score[len(queue)+1]:
                score[len(queue)] += score[len(queue)+1]*2
                score[len(queue) + 1] = 0
            else :
                score[len(queue)] += 2
        elif ss == ']':
            queue.pop()
            if score[len(queue) + 1]:
                score[len(queue)] += score[len(queue) + 1] * 3
                score[len(queue) + 1] = 0
            else:
                score[len(queue)] += 3
    print(score[0])
