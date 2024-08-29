import sys
sys.stdin = open("input.txt", "r")

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        arr = list(map(int, input().split()))
        
        arr_num = arr[0]
        
        size_li = [1] * arr_num
        prev = [-1] * arr_num
        
        for i in range(1, arr_num):
            for j in range(i):
                if arr[i] > arr[j] and size_li[i] < size_li[j] + 1:
                    size_li[i] = size_li[j] + 1
                    prev[i] = j
        
        max_len = max(size_li)
        
        
        print(f"#{test_case} {max_len}")

if __name__ == "__main__":
    main()