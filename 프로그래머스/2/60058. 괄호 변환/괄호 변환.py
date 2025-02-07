def make_two_balanced(w):
    left_cnt, right_cnt = 0, 0
    for idx, p in enumerate(w):
        if p == '(': left_cnt += 1
        elif p == ')' : right_cnt += 1
        
        if left_cnt > 0 and left_cnt == right_cnt:
            return w[:idx+1], w[idx+1:]
def test_right(w):
    stack = []
    for p in w:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack : return False
            stack.pop()
    return True

def solution(p):
    answer = ''
    if not p:
        return answer
    u, v = make_two_balanced(p)
    if test_right(u) : 
        return u + solution(v)
    else:
        u = u[1:-1]
        if not u:
            return '(' + solution(v) + ')'
        new_u = ''
        for pp in u:
            if pp =='(': new_u += ')'
            else : new_u += '('
        return '(' + solution(v) + ')' + new_u
    return answer