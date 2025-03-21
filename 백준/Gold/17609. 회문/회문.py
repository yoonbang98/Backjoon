N = int(input())
for _ in range(N):
    word = input().strip()
    M = len(word)

    left, right = 0, M-1
    paline = True
    flag = False
    while left < right:
        if word[left] != word[right]:
            if right - left == 1:
                flag = True
                break
            paline = False
            break
        else:
            left += 1
            right -= 1
    if paline:
        if flag :
            print(1)
        else:
            print(0)
    else:
        left, right = 0, M-1
        paline2 = True
        cnt = 0
        while left < right:
            if word[left] != word[right]:
                if not cnt :
                    if word[left + 1] == word[right] and left + 1 != right:
                        cnt = 1
                        left += 2
                        right -= 1
                    elif word[left] == word[right-1] and left != right-1:
                        cnt = 1
                        left += 1
                        right -= 2
                    else:
                        paline2 = False
                        break
                else:
                    paline2 = False
                    break
            else:
                left += 1
                right -= 1
        left, right = 0, M-1
        paline3 = True
        cnt = 0
        while left < right:
            if word[left] != word[right]:
                if not cnt :
                    if word[left] == word[right-1] and left != right-1:
                        cnt = 1
                        left += 1
                        right -= 2
                    elif word[left + 1] == word[right] and left + 1 != right:
                        cnt = 1
                        left += 2
                        right -= 1
                    else:
                        paline3 = False
                        break
                else:
                    paline3 = False
                    break
            else:
                left += 1
                right -= 1
        if paline2 or paline3:
            print(1)
        else:
            print(2)