def prev_permutation(seq):
    
    i = n - 2
    while i >= 0 and seq[i] <= seq[i+1]:
        i -= 1

    if i == -1:
        print(-1)
        return
    
    j = n - 1
    while seq[i] <= seq[j]:
        j -= 1

    seq[i], seq[j] = seq[j], seq[i]

    seq[i+1: ] = reversed(seq[i+1: ])
    
    print(*seq)



n = int(input())
seq = list(map(int, input().split()))

prev_permutation(seq)
