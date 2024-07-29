max_num = float("-inf")
min_num = float("inf")

def calc_num(operands, operators, cur_value, idx):
    global max_num
    global min_num

    if sum(operators) == 0:
        max_num = max(max_num, cur_value)
        min_num = min(min_num, cur_value)

    for i in range(4):
        if operators[i] == 0:
            continue

        temp = 0
        if i == 0:
            temp = cur_value + operands[idx]
        elif i == 1:
            temp = cur_value - operands[idx]
        elif i == 2:
            temp = cur_value * operands[idx]
        elif i == 3:
            temp = int(cur_value / operands[idx])

        operators[i] -= 1
        calc_num(operands, operators, temp, idx+1)
        operators[i] += 1



def main():
    num = int(input())
    operands = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    calc_num(operands, operators, operands[0], 1)

    print(max_num)
    print(min_num)




if __name__ == "__main__":
    main()