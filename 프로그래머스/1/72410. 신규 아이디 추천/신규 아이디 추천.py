def solution(new_id):
    answer = ''

    for letter in new_id:
        if letter.isalpha():
            answer += letter.lower()
            continue
        if letter.isalnum() or letter == '.' or letter == '-' or letter == '_':
            if len(answer) and answer[-1] == '.' and letter == '.':
                continue
            answer += letter
        else : 
            continue
    if answer[0] == '.' and len(answer) == 1: 
        answer = 'a'
    if answer[0] == '.' and len(answer) >= 2:
        answer = answer[1:]
    if answer[-1] == '.' and len(answer) >= 2:
        answer = answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]
            
    return answer