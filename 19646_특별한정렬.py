import sys
sys.stdin = open("input.txt", "r")

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        num = int(input())

        arr = list(map(int, input().split()))

        arr.sort()
        result_arr = []

        for i in range(5):
            last_idx = -1-i
            start_idx = i
            result_arr.append(arr[last_idx])
            result_arr.append(arr[start_idx])

        print(f"#{test_case}", end=" ")
        for elem in result_arr:
            print(elem, end=" ")
        print()

if __name__ == "__main__":
    main()