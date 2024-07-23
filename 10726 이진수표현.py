#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt, num = map(int, input().split())
    temp = 0
    is_on = True

    for _ in range(cnt):
        if num == 0:
            temp = 0
        else:
            temp = num % 2
            num = num//2
        if temp == 0:
            is_on = False
            break

    result = ""
    if is_on:
        result="ON"
    else:
        result="OFF"

    print(f"#{test_case} {result}")


