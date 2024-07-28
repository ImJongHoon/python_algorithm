import sys
sys.stdin = open("input.txt", "r")

max_num = float("-inf")
min_num = float("inf")

def calc_num(operator, operand, total_num, idx):
    global max_num
    global min_num

    if sum(operator) == 0:
        #print(f"결과: {total_num} {max_num} {min_num}")
        max_num = max(max_num, total_num)
        min_num = min(min_num, total_num)
    
    #무슨 연산자인가?
    for i in range(4):
        if operator[i] == 0:
            continue

        operator[i] -= 1
        
        if i == 0:
            temp_num = total_num + operand[idx]
        elif i == 1:
            temp_num = total_num - operand[idx]
        elif i == 2:
            temp_num = total_num * operand[idx]
        elif i == 3:
            if operand[idx] == 0:  # 분모가 0인 경우는 계산 X
                return
            temp_num = int(total_num / operand[idx])

        calc_num(operator, operand, temp_num, idx+1)
        operator[i] += 1

def main():
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        global max_num
        global min_num
        max_num = float("-inf")
        min_num = float("inf")

        num = int(input())
        operator = list(map(int, input().split()))
        operand = list(map(int, input().split()))
        #print(operator)
        #print(operand)
        
        
        calc_num(operator, operand, operand[0], 1)


        print(f"#{test_case} {max_num - min_num}")

T = int(input())

if __name__ == "__main__":
    main()