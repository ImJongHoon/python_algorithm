import sys
def main() -> None:
    num = int(sys.stdin.readline())
    num_li = [int(x) for x in sys.stdin.readline().split()]
    min_num = min(num_li)
    max_num = max(num_li)
    print(f"{min_num} {max_num}")
if __name__ == "__main__":
    main()