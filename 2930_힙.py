import heapq
import sys
sys.stdin = open("input.txt", "r")


T = int(input())

def main():
    for test_case in range(1, T + 1):
        num = int(input())

        cal_li = [list(map(int, input().split())) for _ in range(num)]
        #print(cal_li)

        results = []

        #빈 리스트를 최소 힙처럼 다루는 라이브러리
        pq = []

        for li in cal_li:
            if li[0] == 1:
                #최대 힙이라 음수 저장
                heapq.heappush(pq, -li[1])
            elif li[0] == 2:
                if len(pq) == 0:
                    results.append(-1)
                else:
                    results.append(-heapq.heappop(pq))




        print(f"#{test_case} ", end="")
        for elem in results:
            print(elem, end=" ")
        print()

if __name__ == "__main__":
    main()