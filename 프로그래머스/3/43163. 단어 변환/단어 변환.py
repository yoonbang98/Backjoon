from collections import deque, defaultdict
def solution(begin, target, words):
    n = len(begin)
    if target not in words:
        return 0
    visited = defaultdict(int)
    visited[begin] = 1
    queue = deque()
    queue.append(begin)
    while True:
        new_queue = deque()
        while queue:
            cur = queue.popleft()
            for word in words:
                cnt = 0
                for i in range(n):
                    if word[i] != cur[i]:
                        cnt += 1
                if cnt == 1 and not visited[word]:
                    visited[word] = visited[cur] + 1
                    new_queue.append(word)
        if not new_queue: break
        queue = new_queue

    return visited[target] - 1