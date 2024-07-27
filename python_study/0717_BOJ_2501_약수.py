'''
#다양한 형태의 정수 입력
동적이기 때문에 input의 갯수 입력이 무의미해짐.
[한 줄에 정수 하나]
n = int(input())
[한 줄에 특정 개수의 정수] <= 이거 사용
a,b,c,d = map(int, input().split())
[한 줄에 정수 리스트가 주어질 때]
nums = [int(x) for x in input().split()]
[N을 주고 N개 줄의 정수 리스트]
n = int(input())
nums = [int(input()) for _ in range(n)]
[N줄의 2차원 정수 리스트]
n = int(input())
field = [[int(x) for x in input().split()] for i in range(n)]
'''
num, k = map(int, input().split())
def calc(num, k) -> int:
    cnt = 0
    for i in range(num):
        if num % (i+1) == 0:
            cnt += 1
            if(k == cnt):
                return i+1
    return 0
print(calc(num, k))