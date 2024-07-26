import sys
sys.stdin = open("input.txt", "r")

max_val = 0
#중복 확인할 set 생성
global_set = set()
def change_num(num_str, cnt, curr_cnt):
    global max_val
    global global_set

    # 가지치기
    if (num_str, curr_cnt) in global_set:
        return

    #탈출시 max값 비교
    if curr_cnt >= cnt:
        max_val = max(max_val, int(num_str))
        return

    #자리마다
    for i in range(len(num_str)):
        for j in range(len(num_str))[i+1:]:
            print(i, j)
            #문자로 표현된 숫자 변환하는 과정
            temp_str = num_str
            s_list = list(temp_str)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            temp_str = ''.join(s_list)

            # dfs 호출
            change_num(temp_str, cnt, curr_cnt + 1)
            global_set.add((temp_str, curr_cnt+1))

    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def main():
    for test_case in range(1, T + 1):
        global max_val
        global global_set
        global_set = set()

        max_val = 0
        num_str, cnt = input().split()

        #print(num_str, cnt)
        num_set = set()
        change_num(num_str, int(cnt), 0)

        #print(global_set)
        print(f"#{test_case} {max_val}")

main()
