cnt = 0

def dfs(numbers, target, idx, cur_value):
    global cnt
    if idx >= len(numbers):
        if cur_value == target:
            cnt += 1
        return
    dfs(numbers, target, idx + 1, cur_value + numbers[idx])
    dfs(numbers, target, idx + 1, cur_value - numbers[idx])
    
    
def solution(numbers, target):
    global cnt
    answer = 0
    dfs(numbers, target, 0, 0)
    
    answer = cnt
    
    return answer