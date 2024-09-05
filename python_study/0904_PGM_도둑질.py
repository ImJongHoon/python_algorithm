def solution(money):
    answer = 0

    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    #1번 집을 털고, 마지막 집을 털지 않는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])


    #마지막 집을 털고, 1번 집을 털지 않는 경우
    #dp2[-1] = money[-1]
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])


    answer = max(dp1[-2], dp2[-1])

    return answer
