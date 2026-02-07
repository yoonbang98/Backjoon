import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    team_list = list(map(int, sys.stdin.readline().split()))
    score_list = [0]*N
    team_num_list = [0]*201
    for t in team_list:
        team_num_list[t] += 1
    score = 1
    for i in range(N):
        t = team_list[i]
        if team_num_list[t] == 6:
            score_list[i] = score
            score += 1
    score_dict = defaultdict(list)
    for idx, t in enumerate(team_list):
        if not score_list[idx] : continue
        score_dict[t].append(score_list[idx])
    candidate_list = []
    for team_num, team_score_list in score_dict.items():
        candidate_list.append([sum(team_score_list[:4]), team_score_list[4], team_num])

    candidate_list.sort(key = lambda x : (x[0], x[1]))
    print(candidate_list[0][2])