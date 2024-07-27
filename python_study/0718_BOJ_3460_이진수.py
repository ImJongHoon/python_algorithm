'''
import sys
sys.stdin.readline()
=> input() 보다 빠름
'''
import sys
def main() -> None:
    test_case = int(sys.stdin.readline())
    #input을 그냥 반복문만큼 반복
    #nums.append 랑 사실 다를거 없음
    nums = [int(sys.stdin.readline()) for _ in range(test_case)]
    #테스트 케이스만큼 반복
    for num in nums:
        index = 0;
        while(num >= 2):
            if(num % 2 == 1):
                print(index, end=" ")
            num = int(num / 2)
            index += 1
        #마지막
        print(index)
if __name__ == "__main__":
    main()