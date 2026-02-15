import sys
from collections import defaultdict
T = int(sys.stdin.readline())
for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    letter_dict = defaultdict(list)
    for idx, letter in enumerate(W):
        letter_dict[letter].append(idx)
    a1, a2 = len(W) + 1, 0

    for key, val_list in letter_dict.items():
        if len(val_list) < K : continue
        for start in range(0, len(val_list) - K + 1):
            target_idx = val_list[start: start + K]
            a1 = min(a1, target_idx[-1] - target_idx[0] + 1)
            a2 = max(a2, target_idx[-1] - target_idx[0] + 1)
    if a1 != len(W) + 1 and a2 != 0:
        print(a1, a2)
    else:
        print(-1)
