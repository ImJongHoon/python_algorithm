#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

score = 0
def main():
    global score
    score = 0

    for test_case in range(1, T + 1):
        num, size_x, max_point = map(int, input().split())
        board = [list(map(input().split())) for _ in range(num)]

        print(f"#{test_case} {score}")

if __name__ == "__main__":
    main()