import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = input()
    infix = input()
    stack = []

    for element in infix:
        if not stack: #스택이 비었으면
            stack.append(element)
        elif stack[-1] == "+":
            operand = stack.pop()
            operator = stack.pop()

            stack.append(str(int(operator) + int(element)))
        else:
            stack.append(element)

    print(f"#{test_case} {stack.pop()}")
