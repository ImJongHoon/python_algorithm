# import sys
# sys.stdin = open("input.txt", "r")

def main():
    num, goal = map(int, input().split())
    input_li = list(map(int, input().split()))
    min_length = 987654321

    #투포인터로 풀어도 되는가?
    #더한 값이 목표 값보다 크거나 같으면 lp를 증가시키고, 작으면 rp를 증가시키도록
    #어차피 연속되는 수열이라면? 가능할듯
    lp = -1
    rp = -1
    temp_length = 0
    temp_sum = 0

    while rp < num:
        #print(lp, rp, input_li[rp],  temp_sum)
        if temp_sum >= goal:
            #비교하고
            min_length = min(min_length, temp_length)
            #줄이기
            lp += 1
            temp_sum -= input_li[lp]
            temp_length -= 1
        elif temp_sum > goal:
            #줄이기
            lp += 1
            temp_sum -= input_li[lp]
            temp_length -= 1
        elif temp_sum < goal:
            #늘리기
            rp += 1
            if rp == num:
                break
            temp_sum += input_li[rp]
            temp_length += 1
        
    if min_length == 987654321:
        min_length = 0

    print(min_length)

if __name__ == "__main__":
    main()