from collections import deque

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
#16진수
#set => list => 정렬
def main():
    for test_case in range(1, T + 1):
        num, cnt = map(int, input().split())
        input_li = list(input())
        q = deque(input_li)

        length = int(num / 4)
        num_strs = set()

        for _ in range(length):
            q.rotate()
            for i in range(4):
                temp = ''.join(list(q)[i*length:(i+1)*length])
                num_strs.add(temp)

        all_pwd = list(map(lambda x : int(x, 16),list(num_strs)))
        all_pwd.sort(reverse=True)
        #print(f"#{all_pwd}")
        print(f"#{test_case} {all_pwd[cnt-1]}")



if __name__ == "__main__":
    main()