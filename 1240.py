import sys
sys.stdin = open("input.txt", "r")

code_li = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    y, x = map(int, input().split())
    #print(f"y:{y} x:{x}")
    board = [input() for _ in range(y)]

    #뒤에서부터 검사
    code_str = ""

    for str_li in board:
        if code_str != "":
            break
        for idx, code in enumerate(str_li[::-1]):
            if code == "1":
                code_str = str_li[x-idx-56:x-idx]
                #print(len(code))
                break

    code_arr = []
    cal_code = 0
    for i in range(8):
        for idx, cd in enumerate(code_li):
            if code_str[i*7: i*7+7] == cd:
                code_arr.append(idx)
                if idx%2 == 1:
                    cal_code += (idx * 3)
                else:
                    cal_code += idx
                break
                #print(code_arr)
                #print(idx)
    print(code_arr)

    result=0

    if cal_code % 10 == 0:
        result = sum(code_arr)
    else:
        result = 0



    #암호 코드 끝은 다 1로 고정
    print(f"#{test_case} {result}")
