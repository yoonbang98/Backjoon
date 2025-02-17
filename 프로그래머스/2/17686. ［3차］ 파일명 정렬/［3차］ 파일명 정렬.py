
def solution(files):
    answer = []
    name_list = []
    for file in files:
        idx1, idx2 = 0, 0
        for idx, letter in enumerate(file):
            if not idx1 and letter.isnumeric():
                idx1 = idx
            if idx1 and not idx2 and not letter.isnumeric():
                idx2 = idx
        if not idx2 : # tail이 없는 경우
            idx2 = len(file)
        name_list.append([file[:idx1], file[idx1:idx2], file[idx2:]])
    processed_head_number = []
    for idx, (head, number, tail) in enumerate(name_list):
        lower_head = head.lower()
        num = int(number)
        processed_head_number.append([lower_head, num, idx])
    processed_head_number.sort()
    for _, _, idx in processed_head_number:
        head, number, tail = name_list[idx]
        answer.append(head + number + tail)

    return answer