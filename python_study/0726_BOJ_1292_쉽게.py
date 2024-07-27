def main():
    num1, num2 = map(int, input().split())
    #num2까지 다 더한 값 - num1까지 다 더한 합
    sum1 = 0
    sum2 = 0
    add = 1
    cnt = 0
    for num in range(num2+1)[1:]:
        #num1 구하기
        if cnt == add:
            cnt = 0
            add += 1
        #print(add)

        if num <= num1-1:
            sum1 += add
        sum2 += add

        cnt += 1

    print(sum2 - sum1)

    return

if __name__ == "__main__":
    main()