#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_str = list(input())
    #print(input_str)
    stack = []


    #레이저 바꾸면서 넣기
    for bracket in input_str:
        #스택 비었으면
        if not stack:
            stack.append(bracket)
        else:
            if stack[-1] == "(" and bracket == ")": #레이저면
                stack.pop()
                stack.append("0")
            else:
                stack.append(bracket)

    #print(stack)

    # 증가량
    increase = 0
    # 총 갯수
    count = 0
    for element in stack:
        if element == "0":
            count += increase
        elif element == "(":
            increase += 1
        elif element == ")":
            increase -= 1
            count += 1

    print(f"#{test_case} {count}")
