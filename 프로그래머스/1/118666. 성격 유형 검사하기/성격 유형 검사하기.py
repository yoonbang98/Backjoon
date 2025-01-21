def solution(survey, choices):
    score_dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    N = len(survey)
    for i in range(N):
        survey_i = survey[i]
        if choices[i] <= 4: # 비동의 ~ 모르겠음
            score_dict[survey_i[0]] += 4 - choices[i]
        else:
            score_dict[survey_i[1]] += choices[i] - 4
    answer = ''
    if score_dict['R'] >= score_dict['T']:
        answer += 'R'
    else :
        answer += 'T'
    if score_dict['C'] >= score_dict['F']:
        answer += 'C'
    else :
        answer += 'F'
    if score_dict['J'] >= score_dict['M']:
        answer += 'J'
    else :
        answer += 'M'
    if score_dict['A'] >= score_dict['N']:
        answer += 'A'
    else :
        answer += 'N'
    return answer