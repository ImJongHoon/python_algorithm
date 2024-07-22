#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

result = 1
def pal_test(input_str, left, right):
    if left > right:
        return
    else:
        if input_str[left] == input_str[right]:
            pal_test(input_str, left + 1, right - 1)
            return
        else:
            global result
            result = 0


for test_case in range(1, T + 1):
    result = 1

    input_str = input()

    pal_test(input_str, 0, len(input_str)-1)

    print(f"#{test_case} {result}")
