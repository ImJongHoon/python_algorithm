def main():
    day = int(input())
    schedule = [list(map(int, input().split())) for _ in range(day)]

    dp = [0]*(day+1)

    cnt = 0

    for i in range(day):
        cnt = max(cnt, dp[i])
        if i + schedule[i][0] > day:
            continue

        dp[i+schedule[i][0]] = max(cnt + schedule[i][1], dp[i + schedule[i][0]])

    print(max(dp))


if __name__ == "__main__":
    main()