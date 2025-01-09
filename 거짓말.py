import sys
N, M = map(int, sys.stdin.readline().split())
truth = list(map(int, sys.stdin.readline().split()))
party_total = []
for _ in range(M):
    party = list(map(int, sys.stdin.readline().split()))
    party = party[1:]
    party_total.append(party)
parent = [i for i in range(N+1)]
def find(parent, idx):
    if parent[idx] != idx:
        parent[idx] = find(parent, parent[idx])
    return parent[idx]

def union(parent, idx1, idx2):
    r1 = find(parent, idx1)
    r2 = find(parent, idx2)

    if r1 < r2:
        parent[r2] = r1
    else :
        parent[r1] = r2

for party in party_total:
    for i in range(len(party)-1):
        union(parent, party[i], party[i+1])
new_truth = set()
for i in range(1, len(truth)):
    new_truth.add(find(parent,truth[i]))
answer = M
for party in party_total:
    for i in range(len(party)):
        if find(parent, party[i]) in new_truth:
            answer -= 1
            break
print(answer)
