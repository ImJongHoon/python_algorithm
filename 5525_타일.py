#import sys
#sys.stdin = open("input.txt", "r")

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        num = int(input())
        dp = [-1] * (num+1)
        
        dp[1] = 1
        dp[2] = 3
        dp[3] = 6
        
        cur_num = 4
        
        while cur_num <= num:
            dp[cur_num] = dp[cur_num-1] + (2* dp[cur_num-2]) + dp[cur_num-3]
            cur_num += 1
        
        print(f"#{test_case} {dp[num]}")

if __name__ == "__main__":
    main()