import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = input()
    num_arr = [int(x) for x in input().split()]

    pointer_index = 0
    arr_length = len(num_arr)

    counter = 0
    result_arr = []
    while True:
        num_arr[pointer_index] -= (counter+1)
        if num_arr[pointer_index] <= 0:
            num_arr[pointer_index] = 0
            result_arr = num_arr[(pointer_index + 1) % arr_length:] + num_arr[:(pointer_index + 1) % arr_length]
            break

        counter = (counter + 1) % 5
        pointer_index = (pointer_index + 1) % arr_length


    print(f"#{num}", end=" ")
    for elem in result_arr:
        print(elem, end=" ")
    print("")