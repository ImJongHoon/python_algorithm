#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def multi(num, cnt)->int:
    if cnt == 1:
        return num
    else:
        return num * multi(num, cnt-1)

for test_case in range(1, T + 1):
    tc = int(input())
    num, cnt = map(int, input().split())
    print(f"#{tc} {multi(num, cnt)}")


