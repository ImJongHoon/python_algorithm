
T = int(input())

min_count = float("inf")

def main():
    global min_count

    for test_case in range(1, T + 1):
        min_count = float("inf")
        all_num, select_num = map(int, input().split())

        candy_li = list(map(int, input().split()))

        candy_li.sort()

        #print(list(combinations(candy_li, select_num)))
        for i in range(all_num - select_num + 1):
            #print(candy_li[i+select_num-1] - candy_li[i])
            min_count = min(min_count, candy_li[i+select_num-1] - candy_li[i])

        
        #각 사탕의 최대와 최소의 차이를 최소로.

        print(f"#{test_case} {min_count}")

if __name__ == "__main__":
    main()