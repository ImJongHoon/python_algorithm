import sys
#최대공약수
# def great(big_num, small_num):
#     great_num = 0
#     for i in range(1, small_num//2 + 1):
#         if big_num % i == 0 and small_num % i == 0:
#             great_num = i
#     return great_num
#최대공약수 => 유클리드 호재
def great(big_num, small_num):
    num1 = big_num
    num2 = small_num
    temp = 0
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1
#최소 공배수
#두 수 a b의 최소 공배수는 a와 b의 곱을 a와 b의 최대 공약수로 나눈 것과 같다
def least(big_num, small_num, great_num):
    return int((big_num * small_num) / great_num)
def main():
    num1, num2 = map(int, sys.stdin.readline().split())
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    #최대 공약수
    great_num = great(max_num, min_num)
    print(great_num)
    #최소 공배수
    print(least(max_num, min_num, great_num))
if __name__ == "__main__":
    main()