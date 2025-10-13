def dfs(result, n, numbers, target):
    global answer
    if n == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(result + numbers[n], n+1, numbers, target)
    dfs(result - numbers[n], n+1, numbers, target)
    return
        
answer = 0
def solution(numbers, target):
    dfs(numbers[0], 1, numbers, target)
    dfs(-numbers[0], 1, numbers, target)
    
    return answer