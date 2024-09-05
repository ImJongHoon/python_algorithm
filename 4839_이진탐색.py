#import sys
#sys.stdin = open("input.txt", "r")

def bs(max_page, target):
    cnt = 1

    lp = 1
    rp = max_page
    center = int((lp + rp) / 2)

    while center != target:
        if center > target:
            rp = center
        else:
            lp = center
        
        center = int((lp + rp) / 2)
        cnt += 1

    return cnt


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        max_page, std1, std2 = map(int, input().split())

        std1_cnt = bs(max_page, std1)
        std2_cnt = bs(max_page, std2)

        result = "0"

        if std1_cnt < std2_cnt:
            result = "A"
        elif std2_cnt < std1_cnt:
            result = "B"

        print(f"#{test_case} {result}")

if __name__ == "__main__":
    main()