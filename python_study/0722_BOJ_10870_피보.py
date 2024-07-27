#재귀함수 사용
import sys
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(sys.stdin.readline())
print(fibonacci(num))
#메모이제이션 사용한 최적화
import sys
num = int(sys.stdin.readline())
#list 할당문
memo = [0] * (num+1)
def fibonacci(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
memo[0] = 0
if num > 0:
    memo[1] = 1
print(fibonacci(num))