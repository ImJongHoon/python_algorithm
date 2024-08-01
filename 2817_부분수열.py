#import sys
#sys.stdin = open("input.txt", "r")

cnt = 0

def DFS(num_li, goal, idx, sum):
    global cnt

    
    if idx >= len(num_li) :
        return
    
    if sum == goal:
        cnt += 1
        return
    #print(sum)
    
    DFS(num_li, goal, idx + 1, sum + num_li[idx])
    DFS(num_li, goal, idx + 1, sum)


T = int(input())
def main():
    global cnt

    for test_case in range(1, T + 1):
        cnt = 0
        num, goal = map(int, input().split())
        num_li = list(map(int, input().split()))
        DFS(num_li, goal, 0, 0)
        DFS(num_li, goal, 0, num_li[0])

        print(f"#{test_case} {cnt}")


if __name__ == "__main__":
    main()